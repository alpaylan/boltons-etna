"""Property functions for the boltons ETNA workload.

Each property is pure, total, deterministic. Returns PropertyResult.
"""
from __future__ import annotations

from datetime import date, timedelta
from itertools import islice
from typing import List, Tuple

from boltons.cacheutils import LRI
from boltons.dictutils import OneToOne, OrderedMultiDict as OMD
from boltons.iterutils import remap
from boltons.listutils import BarrelList
from boltons.mathutils import Bits
from boltons.setutils import IndexedSet
from boltons.statsutils import Stats
from boltons.strutils import bytes2human, singularize
from boltons.tableutils import Table
from boltons.timeutils import daterange

from ._result import PASS, DISCARD, PropertyResult, fail


# ---------------------------------------------------------------------------
# 1. BarrelListSortPreservesElements (variant: barrellist_sort_drops_lists_b8855d7_1)
# ---------------------------------------------------------------------------
def property_barrel_list_sort_preserves_elements(
    args: Tuple[List[int], List[int]],
) -> PropertyResult:
    """``BarrelList.sort()`` must preserve all elements when there are
    multiple internal lists.

    Bug (b8855d7): after ``del self.lists[:]`` the buggy code did
    ``self.lists[0] = tmp_sorted`` against an empty list — IndexError.
    """
    list_a, list_b = args
    bl = BarrelList()
    # Replace internal storage to force ``len(self.lists) > 1`` branch.
    bl.lists = [list(list_a), list(list_b)]
    expected = sorted(list(list_a) + list(list_b))
    try:
        bl.sort()
    except Exception as e:  # noqa: BLE001 — surface the panic
        return fail(
            f"BarrelList.sort({list_a!r}, {list_b!r}) raised "
            f"{type(e).__name__}: {e}"
        )
    actual = list(bl)
    if actual != expected:
        return fail(
            f"BarrelList.sort({list_a!r}, {list_b!r}): "
            f"got {actual!r}, expected {expected!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# 2. TableToTextColumnsAlign (variant: table_to_text_row_widths_0c88f25_1)
# ---------------------------------------------------------------------------
def property_table_to_text_columns_align(
    args: List[Tuple[str, str]],
) -> PropertyResult:
    """``Table.to_text(with_headers=False)`` should pad each column to the
    width of the widest cell in that column.

    Bug (0c88f25): the buggy implementation measured ``len(row)`` (number of
    cells) instead of ``len(row[idx])`` (str length), giving every column the
    same constant width equal to the row count, which leaves long cells
    unpadded and short cells over-padded.
    """
    rows = args
    if not rows:
        return DISCARD
    # Two-column table; require strings to be ASCII-printable, no pipes.
    for r in rows:
        for cell in r:
            if "|" in cell or "\n" in cell:
                return DISCARD
    table = Table.from_data([list(r) for r in rows])
    out = table.to_text(with_headers=False)
    expected_widths = [
        max(len(rows[i][j]) for i in range(len(rows))) for j in range(2)
    ]
    lines = out.splitlines()
    if len(lines) != len(rows):
        return fail(
            f"to_text({rows!r}): got {len(lines)} lines, expected {len(rows)}"
        )
    for li, line in enumerate(lines):
        cells = line.split(" | ")
        if len(cells) != 2:
            return fail(
                f"to_text({rows!r}) line {li}: split produced "
                f"{len(cells)} cells (line={line!r})"
            )
        for j in range(2):
            if len(cells[j]) != expected_widths[j]:
                return fail(
                    f"to_text({rows!r}) line {li} col {j}: "
                    f"width={len(cells[j])}, expected {expected_widths[j]}"
                )
    return PASS


# ---------------------------------------------------------------------------
# 3. OneToOneUpdateEmptyOk (variant: onetoone_update_unbound_keys_vals_6cac49c_1)
# ---------------------------------------------------------------------------
def property_one_to_one_update_empty_ok(args: int) -> PropertyResult:
    """``OneToOne.update`` must accept an empty mapping/iterable without
    raising.

    Bug (6cac49c): without ``keys_vals = []`` initialisation, ``update({})``
    falls through to ``keys_vals.extend(...)`` while ``keys_vals`` is
    unbound, raising UnboundLocalError.
    """
    seed = args
    ot = OneToOne({"a": "b"})
    # Update with an empty dict.
    try:
        ot.update({})
    except Exception as e:  # noqa: BLE001
        return fail(
            f"OneToOne.update({{}}) raised {type(e).__name__}: {e}"
        )
    # Update with an empty iterable.
    try:
        ot.update([])
    except Exception as e:  # noqa: BLE001
        return fail(
            f"OneToOne.update([]) raised {type(e).__name__}: {e}"
        )
    if ot.get("a") != "b":
        return fail(f"OneToOne lost prior contents after empty update: {dict(ot)!r}")
    # Sanity: a non-empty update still works.
    ot.update({"x": "y"})
    if ot.get("x") != "y":
        return fail(f"OneToOne.update({{'x':'y'}}) failed: {dict(ot)!r}")
    return PASS


# ---------------------------------------------------------------------------
# 4. BitsAsListLengthMatches (variant: bits_as_list_truncates_zero_pad_40a7b47_1)
# ---------------------------------------------------------------------------
def property_bits_as_list_length_matches(args: Tuple[int, int]) -> PropertyResult:
    """``Bits(val, n).as_list()`` must always have length ``n``.

    Bug (40a7b47): unpadded ``'{0:b}'.format(val)`` collapsed leading zeros,
    so ``Bits(0, 2).as_list()`` returned ``[False]`` instead of
    ``[False, False]``.
    """
    val, n = args
    if not (n >= 1 and 0 <= val < (1 << n)):
        return DISCARD
    b = Bits(val, n)
    bl = b.as_list()
    if len(bl) != n:
        return fail(
            f"Bits({val}, {n}).as_list(): len={len(bl)}, expected {n} "
            f"(got {bl!r})"
        )
    # Round-trip check.
    if list(b) != bl:
        return fail(
            f"Bits({val}, {n}): list(b)={list(b)!r} != as_list()={bl!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# 5. DaterangeSameStartStopTerminates (variant: daterange_inclusive_same_start_stop_93185b2_1)
# ---------------------------------------------------------------------------
def property_daterange_same_start_stop_terminates(args: int) -> PropertyResult:
    """``daterange(d, d, inclusive=True)`` must terminate.

    Bug (93185b2): ``elif start < stop`` (strict) caused start==stop to
    fall through to the descending branch, where ``operator.lt(d, d)`` is
    False forever — infinite generator.
    """
    days = args
    if not (-3650 <= days <= 3650):
        return DISCARD
    base = date(2025, 1, 1)
    d = base + timedelta(days=days)
    try:
        result = list(islice(daterange(d, d, inclusive=True), 5))
    except Exception as e:  # noqa: BLE001
        return fail(
            f"daterange({d}, {d}, inclusive=True) raised "
            f"{type(e).__name__}: {e}"
        )
    if len(result) > 1:
        return fail(
            f"daterange({d}, {d}, inclusive=True): produced "
            f"{len(result)} dates ({result!r}), expected ≤ 1"
        )
    if len(result) == 1 and result[0] != d:
        return fail(
            f"daterange({d}, {d}, inclusive=True): first={result[0]}, "
            f"expected {d}"
        )
    # Non-inclusive: must yield zero dates.
    try:
        result_excl = list(islice(daterange(d, d, inclusive=False), 5))
    except Exception as e:  # noqa: BLE001
        return fail(
            f"daterange({d}, {d}, inclusive=False) raised "
            f"{type(e).__name__}: {e}"
        )
    if result_excl:
        return fail(
            f"daterange({d}, {d}, inclusive=False): produced "
            f"{result_excl!r}, expected []"
        )
    return PASS


# ---------------------------------------------------------------------------
# 6. IndexedSetIndexAfterRemovals (variant: indexed_set_index_ignores_dead_4457dec_1)
# ---------------------------------------------------------------------------
def property_indexed_set_index_after_removals(
    args: Tuple[List[int], List[int]],
) -> PropertyResult:
    """For an ``IndexedSet`` after some pops, ``iset.index(x)`` must return
    the *apparent* (post-removal) index — not a position from before the
    removals.

    Bug (4457dec): ``index(val)`` returned ``self.item_index_map[val]``
    directly, which carries the pre-removal position; ``iset[idx]`` then
    yielded a different item.
    """
    items, drop_seeds = args
    # Dedup (IndexedSet rejects duplicates).
    seen = set()
    uniq = []
    for x in items:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    if len(uniq) < 2:
        return DISCARD
    iset = IndexedSet(uniq)
    # Pop a deterministic subset, but always leave at least 1 item alive.
    drops = []
    for s in drop_seeds[:]:
        if len(iset) <= 1:
            break
        drops.append(s % len(iset))
        iset.pop(drops[-1])
    if not iset:
        return DISCARD
    items_now = list(iset)
    for i, x in enumerate(items_now):
        idx = iset.index(x)
        if idx != i:
            return fail(
                f"IndexedSet({uniq!r}) after pops {drops!r}: "
                f"iset.index({x!r})={idx} but list(iset)[{i}]={x!r}"
            )
    return PASS


# ---------------------------------------------------------------------------
# 7. SingularizeSensesIsSense (variant: singularize_senses_to_sens_d056712_1)
# ---------------------------------------------------------------------------
def property_singularize_senses_is_sense(args: int) -> PropertyResult:
    """``singularize('senses')`` must produce ``'sense'`` (irregular case).

    Bug (d056712): without 'sense' → 'senses' in the irregular-pluralization
    table, the algorithm strips the trailing 's' to produce 'sens'.
    """
    _ = args
    actual = singularize("senses")
    if actual != "sense":
        return fail(
            f"singularize('senses') = {actual!r}, expected 'sense'"
        )
    return PASS


# ---------------------------------------------------------------------------
# 8. OmdSetdefaultReturnsStored (variant: omd_setdefault_returns_default_b1df971_1)
# ---------------------------------------------------------------------------
def property_omd_setdefault_returns_stored(args: int) -> PropertyResult:
    """``OMD.setdefault(k, v)`` must store *v* (not ``[v]``) and return the
    stored value, including ``None`` when no default is given.

    Bug (b1df971): the old code stored ``[default]`` and returned the raw
    sentinel ``_MISSING``/``default`` instead of the stored value.
    """
    val = args
    omd = OMD()
    ret = omd.setdefault("k", val)
    stored = omd["k"]
    if stored != val:
        return fail(
            f"OMD.setdefault('k', {val!r}): omd['k']={stored!r}, "
            f"expected {val!r}"
        )
    if ret != val:
        return fail(
            f"OMD.setdefault('k', {val!r}) returned {ret!r}, expected {val!r}"
        )
    omd2 = OMD()
    ret_none = omd2.setdefault("q")
    if ret_none is not None:
        return fail(
            f"OMD.setdefault('q') returned {ret_none!r}, expected None"
        )
    if omd2["q"] is not None:
        return fail(
            f"OMD.setdefault('q'): omd['q']={omd2['q']!r}, expected None"
        )
    return PASS


# ---------------------------------------------------------------------------
# 9. DaterangeInfiniteIterates (variant: daterange_finished_arity_mismatch_139d5dc_1)
# ---------------------------------------------------------------------------
def property_daterange_infinite_iterates(args: int) -> PropertyResult:
    """``daterange(d, None)`` must yield consecutive dates without raising.

    Bug (139d5dc): the unbounded-stop branch installed a 1-arg lambda
    while the bounded branches install 2-arg lambdas; the inner ``while
    not finished(now, stop)`` then raises TypeError on the first call.
    """
    days = args
    if not (-3650 <= days <= 3650):
        return DISCARD
    today = date(2025, 1, 1) + timedelta(days=days)
    try:
        gen = daterange(today, None)
        first = next(gen)
        second = next(gen)
        third = next(gen)
    except Exception as e:  # noqa: BLE001
        return fail(
            f"daterange({today}, None): raised "
            f"{type(e).__name__}: {e}"
        )
    if first != today:
        return fail(
            f"daterange({today}, None): first={first}, expected {today}"
        )
    if second != today + timedelta(days=1):
        return fail(
            f"daterange({today}, None): second={second}, "
            f"expected {today + timedelta(days=1)}"
        )
    if third != today + timedelta(days=2):
        return fail(
            f"daterange({today}, None): third={third}, "
            f"expected {today + timedelta(days=2)}"
        )
    return PASS


# ---------------------------------------------------------------------------
# 10. Bytes2HumanIsRepeatable (variant: bytes2human_size_ranges_consumed_0082e13_1)
# ---------------------------------------------------------------------------
def property_bytes2_human_is_repeatable(args: int) -> PropertyResult:
    """Repeated calls to ``bytes2human(n)`` must return the same string.

    Bug (0082e13): ``_SIZE_RANGES = zip(...)`` is a one-shot iterator; the
    first call drains it, the second sees an empty iterator and either
    UnboundLocalErrors on ``size`` or returns wrong output.
    """
    n_seed = args
    if n_seed < 0:
        return DISCARD
    n = n_seed
    try:
        first = bytes2human(n)
        second = bytes2human(n)
        third = bytes2human(n + 1)
    except Exception as e:  # noqa: BLE001
        return fail(
            f"bytes2human({n}) raised {type(e).__name__}: {e}"
        )
    if first != second:
        return fail(
            f"bytes2human({n}) repeated: first={first!r}, second={second!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# 11. RemapPreservesSet (variant: remap_set_passes_pairs_to_update_f74b7e5_1)
# ---------------------------------------------------------------------------
def property_remap_preserves_set(args: List[int]) -> PropertyResult:
    """``remap(s)`` of a set must equal ``s``.

    Bug (f74b7e5): the buggy ``default_exit`` passed ``new_items``
    (``[(0, v0), (1, v1), ...]``) to ``set.update``, ending up with a set
    of 2-tuples instead of the original elements.
    """
    items = args
    s = set(items)
    out = remap(s)
    if out != s:
        return fail(
            f"remap({s!r}) = {out!r}, expected {s!r}"
        )
    fs = frozenset(items)
    fs_out = remap(fs)
    if fs_out != fs:
        return fail(
            f"remap({fs!r}) = {fs_out!r}, expected {fs!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# 12. OmdEqHandlesNonIterable (variant: omd_eq_raises_on_non_iterable_31873ae_1)
# ---------------------------------------------------------------------------
def property_omd_eq_handles_non_iterable(
    args: Tuple[List[Tuple[int, int]], int],
) -> PropertyResult:
    """``OMD == non_iterable`` must return False instead of raising.

    Bug (31873ae): ``len(other) != len(self)`` raises ``TypeError`` when
    ``other`` is something like an int; ``__eq__`` propagated that.
    """
    items, other = args
    omd = OMD()
    for k, v in items:
        omd.add(k, v)
    try:
        result = omd == other
    except Exception as e:  # noqa: BLE001
        return fail(
            f"OMD == {other!r} raised {type(e).__name__}: {e}"
        )
    if result is not False:
        return fail(
            f"OMD({items!r}) == {other!r} returned {result!r}, expected False"
        )
    try:
        ne_result = omd != other
    except Exception as e:  # noqa: BLE001
        return fail(
            f"OMD != {other!r} raised {type(e).__name__}: {e}"
        )
    if ne_result is not True:
        return fail(
            f"OMD({items!r}) != {other!r} returned {ne_result!r}, expected True"
        )
    return PASS


# ---------------------------------------------------------------------------
# 13. StatsQuantileEmptyReturnsDefault (variant: stats_quantile_empty_raises_a13bfb1_1)
# ---------------------------------------------------------------------------
def property_stats_quantile_empty_returns_default(args: int) -> PropertyResult:
    """``Stats([]).get_quantile(q)`` must return ``self.default`` instead of
    raising.

    Bug (a13bfb1): without the empty-data guard, the inner quantile path
    indexed into ``[]`` (IndexError) or divided by zero.
    """
    q_pct = args
    if not (0 <= q_pct <= 100):
        return DISCARD
    q = q_pct / 100.0
    s = Stats([])
    try:
        result = s.get_quantile(q)
    except Exception as e:  # noqa: BLE001
        return fail(
            f"Stats([]).get_quantile({q}) raised {type(e).__name__}: {e}"
        )
    if result != s.default:
        return fail(
            f"Stats([]).get_quantile({q}) = {result!r}, "
            f"expected default={s.default!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# 14. LruReprFieldOrder (variant: lru_repr_swaps_max_size_on_miss_bad95b6_1)
# ---------------------------------------------------------------------------
def property_lru_repr_field_order(args: int) -> PropertyResult:
    """``repr(LRI(max_size=n))`` must contain ``max_size=<n>`` (the
    integer), not ``max_size=<callable_or_None>``.

    Bug (bad95b6): the ``%`` interpolation argument order was swapped, so
    ``max_size`` got bound to ``self.on_miss`` and vice-versa.
    """
    n = args
    if not (1 <= n <= 1024):
        return DISCARD
    lri = LRI(max_size=n)
    r = repr(lri)
    expected = f"max_size={n}"
    if expected not in r:
        return fail(
            f"LRI(max_size={n}): repr={r!r}, missing {expected!r}"
        )
    if "on_miss=None" not in r:
        return fail(
            f"LRI(max_size={n}): repr={r!r}, missing 'on_miss=None'"
        )
    return PASS
