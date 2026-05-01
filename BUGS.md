# boltons — Injected Bugs

Pure-Python utility belt — bug fixes mined from upstream history.

Total mutations: 14

## Bug Index

| # | Variant | Name | Location | Injection | Fix Commit |
|---|---------|------|----------|-----------|------------|
| 1 | `barrellist_sort_drops_lists_b8855d7_1` | `barrellist_sort_drops_lists` | `boltons/listutils.py:311` | `patch` | `b8855d768baef2f14d832becdfdfa3bee7c9380d` |
| 2 | `bits_as_list_truncates_zero_pad_40a7b47_1` | `bits_as_list_truncates_zero_pad` | `boltons/mathutils.py:206` | `patch` | `40a7b47c6e8235a1b2a4600d0ceec4f7ea0f9bb0` |
| 3 | `bytes2human_size_ranges_consumed_0082e13_1` | `bytes2human_size_ranges_consumed` | `boltons/strutils.py:548` | `patch` | `0082e13048dcf1574d4163ccc20b67b8a593277a` |
| 4 | `daterange_finished_arity_mismatch_139d5dc_1` | `daterange_finished_arity_mismatch` | `boltons/timeutils.py:370` | `patch` | `139d5dcd3255eddb822aa2d876ce3120c34d81c7` |
| 5 | `daterange_inclusive_same_start_stop_93185b2_1` | `daterange_inclusive_same_start_stop` | `boltons/timeutils.py:371` | `patch` | `93185b224ebd60df01df88d64e574a3f651987c5` |
| 6 | `indexed_set_index_ignores_dead_4457dec_1` | `indexed_set_index_ignores_dead` | `boltons/setutils.py:465` | `patch` | `4457decc614ee795804f2bb9c44ae9be30831d53` |
| 7 | `lru_repr_swaps_max_size_on_miss_bad95b6_1` | `lru_repr_swaps_max_size_on_miss` | `boltons/cacheutils.py:329` | `patch` | `bad95b645c5fb7d14e02ad6ae479f1a05bc8185e` |
| 8 | `omd_eq_raises_on_non_iterable_31873ae_1` | `omd_eq_raises_on_non_iterable` | `boltons/dictutils.py:342` | `patch` | `31873aebe9df299df76053f7f2e6527ae013de9a` |
| 9 | `omd_setdefault_returns_default_b1df971_1` | `omd_setdefault_returns_default` | `boltons/dictutils.py:261` | `patch` | `b1df97114e94f930a28b18e756c1df436ea1ac85` |
| 10 | `onetoone_update_unbound_keys_vals_6cac49c_1` | `onetoone_update_unbound_keys_vals` | `boltons/dictutils.py:874` | `patch` | `6cac49ce4eba506a3582e8089bcc347c6b2fa70f` |
| 11 | `remap_set_passes_pairs_to_update_f74b7e5_1` | `remap_set_passes_pairs_to_update` | `boltons/iterutils.py:1083` | `patch` | `f74b7e5a7d6cc985d47540c4437a072da6803851` |
| 12 | `singularize_senses_to_sens_d056712_1` | `singularize_senses_to_sens` | `boltons/strutils.py:300` | `patch` | `d056712a4a2abcdb977a6e9a3f80bef0fcaadedd` |
| 13 | `stats_quantile_empty_raises_a13bfb1_1` | `stats_quantile_empty_raises` | `boltons/statsutils.py:475` | `patch` | `a13bfb16fbf4f53ae23fb20cdafb69547fae8a02` |
| 14 | `table_to_text_row_widths_0c88f25_1` | `table_to_text_row_widths` | `boltons/tableutils.py:572` | `patch` | `0c88f25323de3ff85bcca844b9ce6cd171a80392` |

## Property Mapping

| Variant | Property | Witness(es) |
|---------|----------|-------------|
| `barrellist_sort_drops_lists_b8855d7_1` | `BarrelListSortPreservesElements` | `witness_barrel_list_sort_preserves_elements_case_basic` |
| `bits_as_list_truncates_zero_pad_40a7b47_1` | `BitsAsListLengthMatches` | `witness_bits_as_list_length_matches_case_zero_pad` |
| `bytes2human_size_ranges_consumed_0082e13_1` | `Bytes2HumanIsRepeatable` | `witness_bytes2_human_is_repeatable_case_one_kib` |
| `daterange_finished_arity_mismatch_139d5dc_1` | `DaterangeInfiniteIterates` | `witness_daterange_infinite_iterates_case_today` |
| `daterange_inclusive_same_start_stop_93185b2_1` | `DaterangeSameStartStopTerminates` | `witness_daterange_same_start_stop_terminates_case_zero_offset` |
| `indexed_set_index_ignores_dead_4457dec_1` | `IndexedSetIndexAfterRemovals` | `witness_indexed_set_index_after_removals_case_pop_one` |
| `lru_repr_swaps_max_size_on_miss_bad95b6_1` | `LruReprFieldOrder` | `witness_lru_repr_field_order_case_basic` |
| `omd_eq_raises_on_non_iterable_31873ae_1` | `OmdEqHandlesNonIterable` | `witness_omd_eq_handles_non_iterable_case_int` |
| `omd_setdefault_returns_default_b1df971_1` | `OmdSetdefaultReturnsStored` | `witness_omd_setdefault_returns_stored_case_basic` |
| `onetoone_update_unbound_keys_vals_6cac49c_1` | `OneToOneUpdateEmptyOk` | `witness_one_to_one_update_empty_ok_case_basic` |
| `remap_set_passes_pairs_to_update_f74b7e5_1` | `RemapPreservesSet` | `witness_remap_preserves_set_case_three_ints` |
| `singularize_senses_to_sens_d056712_1` | `SingularizeSensesIsSense` | `witness_singularize_senses_is_sense_case_basic` |
| `stats_quantile_empty_raises_a13bfb1_1` | `StatsQuantileEmptyReturnsDefault` | `witness_stats_quantile_empty_returns_default_case_median` |
| `table_to_text_row_widths_0c88f25_1` | `TableToTextColumnsAlign` | `witness_table_to_text_columns_align_case_uneven` |

## Framework Coverage

| Property | proptest | quickcheck | crabcheck | hegel |
|----------|---------:|-----------:|----------:|------:|
| `BarrelListSortPreservesElements` | ✓ | ✓ | ✓ | ✓ |
| `BitsAsListLengthMatches` | ✓ | ✓ | ✓ | ✓ |
| `Bytes2HumanIsRepeatable` | ✓ | ✓ | ✓ | ✓ |
| `DaterangeInfiniteIterates` | ✓ | ✓ | ✓ | ✓ |
| `DaterangeSameStartStopTerminates` | ✓ | ✓ | ✓ | ✓ |
| `IndexedSetIndexAfterRemovals` | ✓ | ✓ | ✓ | ✓ |
| `LruReprFieldOrder` | ✓ | ✓ | ✓ | ✓ |
| `OmdEqHandlesNonIterable` | ✓ | ✓ | ✓ | ✓ |
| `OmdSetdefaultReturnsStored` | ✓ | ✓ | ✓ | ✓ |
| `OneToOneUpdateEmptyOk` | ✓ | ✓ | ✓ | ✓ |
| `RemapPreservesSet` | ✓ | ✓ | ✓ | ✓ |
| `SingularizeSensesIsSense` | ✓ | ✓ | ✓ | ✓ |
| `StatsQuantileEmptyReturnsDefault` | ✓ | ✓ | ✓ | ✓ |
| `TableToTextColumnsAlign` | ✓ | ✓ | ✓ | ✓ |

## Bug Details

### 1. barrellist_sort_drops_lists

- **Variant**: `barrellist_sort_drops_lists_b8855d7_1`
- **Location**: `boltons/listutils.py:311` (inside `BarrelList.sort`)
- **Property**: `BarrelListSortPreservesElements`
- **Witness(es)**:
  - `witness_barrel_list_sort_preserves_elements_case_basic` — Two internal lists; sort must not raise and must preserve elements
- **Source**: internal — Fix barrellist sort with multiple lists
  > ``BarrelList.sort()`` cleared ``self.lists`` via ``del self.lists[:]`` and then assigned ``self.lists[0] = tmp_sorted`` — but ``self.lists`` is now empty, so the indexed assignment raises IndexError. The fix uses ``self.lists.append(tmp_sorted)`` instead. Reproduces only when there are multiple internal lists (i.e. the BarrelList has spilled past one bucket).
- **Fix commit**: `b8855d768baef2f14d832becdfdfa3bee7c9380d` — Fix barrellist sort with multiple lists
- **Invariant violated**: When a ``BarrelList`` has more than one internal list, ``bl.sort()`` produces an output whose ``list(bl)`` equals ``sorted(<original elements>)``, without raising.
- **How the mutation triggers**: The mutation reverts the ``self.lists.append(tmp_sorted)`` line to ``self.lists[0] = tmp_sorted``. Because ``del self.lists[:]`` runs immediately before, the indexed assignment hits an empty list and raises IndexError.

### 2. bits_as_list_truncates_zero_pad

- **Variant**: `bits_as_list_truncates_zero_pad_40a7b47_1`
- **Location**: `boltons/mathutils.py:206` (inside `Bits.as_list`)
- **Property**: `BitsAsListLengthMatches`
- **Witness(es)**:
  - `witness_bits_as_list_length_matches_case_zero_pad` — Bits(0, 2): expected [False, False]; bug returns [False]
- **Source**: [#315](https://github.com/mahmoud/boltons/pull/315) — bugfix in mathutils.Bits.as_list (#315)
  > ``Bits.as_list`` formatted the integer with ``'{0:b}'`` (no leading zero pad), so values whose binary representation was shorter than ``self.len`` came out truncated. ``Bits(0, 2).as_list()`` returned ``[False]`` instead of ``[False, False]``. The fix reuses ``self.as_bin()`` which zero-pads to ``self.len``.
- **Fix commit**: `40a7b47c6e8235a1b2a4600d0ceec4f7ea0f9bb0` — bugfix in mathutils.Bits.as_list (#315)
- **Invariant violated**: For all ``Bits(val, n)`` with ``0 <= val < 2**n``, ``len(Bits(val, n).as_list()) == n`` and ``list(Bits(val, n)) == Bits(val, n).as_list()``.
- **How the mutation triggers**: The mutation reverts ``as_list`` to ``[c == '1' for c in '{0:b}'.format(self.val)]``. The unpadded format strips leading zeros, so for values with fewer significant bits than ``self.len`` the returned list is shorter than ``n``.

### 3. bytes2human_size_ranges_consumed

- **Variant**: `bytes2human_size_ranges_consumed_0082e13_1`
- **Location**: `boltons/strutils.py:548` (inside `_SIZE_RANGES`)
- **Property**: `Bytes2HumanIsRepeatable`
- **Witness(es)**:
  - `witness_bytes2_human_is_repeatable_case_one_kib` — Two consecutive 1024-byte calls; the second observes the drained iterator
- **Source**: internal — Fix bytes2human when builtin zip returns iterators
  > Module-level ``_SIZE_RANGES = zip(...)`` was a one-shot iterator under Python 3 (zip returns an iterator, not a list). The first call to ``bytes2human`` drained it; subsequent calls saw an empty iterable, fell out of the size-bucket loop with ``size`` and ``symbol`` unbound, and raised UnboundLocalError. The fix wraps ``zip`` in ``list``.
- **Fix commit**: `0082e13048dcf1574d4163ccc20b67b8a593277a` — Fix bytes2human when builtin zip returns iterators
- **Invariant violated**: ``bytes2human(n)`` is referentially transparent: every invocation with the same input returns the same string, regardless of how many times it has been called before.
- **How the mutation triggers**: The mutation reverts ``_SIZE_RANGES`` to the unwrapped ``zip(...)`` iterator. The first call iterates and drains it; the second call's ``for ... in _SIZE_RANGES`` immediately exits, leaving ``size`` unbound — UnboundLocalError on the divide.

### 4. daterange_finished_arity_mismatch

- **Variant**: `daterange_finished_arity_mismatch_139d5dc_1`
- **Location**: `boltons/timeutils.py:370` (inside `daterange`)
- **Property**: `DaterangeInfiniteIterates`
- **Witness(es)**:
  - `witness_daterange_infinite_iterates_case_today` — Three pulls verify both the first and the inner-loop termination calls
- **Source**: internal — Fix bug in implementation of `timeutils.daterange`
  > ``daterange`` installs a ``finished`` predicate to terminate the inner loop. With ``stop=None`` the predicate was a 1-arg lambda; with bounded ``stop`` it was 2-arg. The dispatch ``while not finished(now, stop)`` then crashed for the unbounded case. The fix gives both branches the same ``(now, stop) -> bool`` signature.
- **Fix commit**: `139d5dcd3255eddb822aa2d876ce3120c34d81c7` — Fix bug in implementation of `timeutils.daterange`
- **Invariant violated**: ``daterange(d, None)`` yields a sequence starting at ``d``, ``d+1``, ``d+2``, ... without raising on any pull.
- **How the mutation triggers**: The mutation reverts the unbounded-stop predicate to ``lambda t: False``. The first call inside the generator's main loop is ``finished(now, stop)`` (two args) — TypeError before the first yield.

### 5. daterange_inclusive_same_start_stop

- **Variant**: `daterange_inclusive_same_start_stop_93185b2_1`
- **Location**: `boltons/timeutils.py:371` (inside `daterange`)
- **Property**: `DaterangeSameStartStopTerminates`
- **Witness(es)**:
  - `witness_daterange_same_start_stop_terminates_case_zero_offset` — Bounded islice keeps the test from hanging on the infinite branch
- **Source**: [#302](https://github.com/mahmoud/boltons/pull/302) — Fix infinite daterange issue when start and stop is same (#302)
  > ``daterange(d, d, inclusive=True)`` looped forever. The branch selection used a strict ``elif start < stop``, so when ``start == stop`` it fell through to the descending branch with ``finished = operator.lt`` — and ``operator.lt(d, d)`` is always False. The fix relaxes to ``elif start <= stop`` so the equal case picks the ascending termination predicate.
- **Fix commit**: `93185b224ebd60df01df88d64e574a3f651987c5` — Fix infinite daterange issue when start and stop is same (#302)
- **Invariant violated**: ``daterange(d, d, inclusive=True)`` yields exactly ``[d]`` and then terminates; ``daterange(d, d, inclusive=False)`` yields ``[]`` and terminates.
- **How the mutation triggers**: The mutation tightens ``start <= stop`` back to ``start < stop``. With equal endpoints the branch chooses the descending termination test (``operator.lt`` for inclusive=True), which never fires; the generator is infinite.

### 6. indexed_set_index_ignores_dead

- **Variant**: `indexed_set_index_ignores_dead_4457dec_1`
- **Location**: `boltons/setutils.py:465` (inside `IndexedSet.index`)
- **Property**: `IndexedSetIndexAfterRemovals`
- **Witness(es)**:
  - `witness_indexed_set_index_after_removals_case_pop_one` — 20-item set; popping a middle index leaves dead_indices populated
- **Source**: [#240](https://github.com/mahmoud/boltons/issues/240) — fix IndexedSet.index() to account for removals, fixes #240
  > ``IndexedSet.index(val)`` returned ``self.item_index_map[val]`` directly. That raw position carries any pre-removal slot the value used to occupy; with un-compacted ``dead_indices`` the apparent index has shifted and the returned value is wrong. The fix routes the lookup through ``self._get_apparent_index`` so the post-removal index is reported.
- **Fix commit**: `4457decc614ee795804f2bb9c44ae9be30831d53` — fix IndexedSet.index() to account for removals, fixes #240
- **Invariant violated**: For an ``IndexedSet`` with any removals, ``iset[iset.index(x)] == x`` for every ``x`` still in the set.
- **How the mutation triggers**: The mutation drops the ``_get_apparent_index`` call. With the ``IndexedSet`` short of its compaction threshold (``dead_count <= len/_COMPACTION_FACTOR``), ``dead_indices`` survives across calls and ``index`` returns the pre-removal slot, off-by-(number of dead intervals before that slot).

### 7. lru_repr_swaps_max_size_on_miss

- **Variant**: `lru_repr_swaps_max_size_on_miss_bad95b6_1`
- **Location**: `boltons/cacheutils.py:329` (inside `LRI.__repr__`)
- **Property**: `LruReprFieldOrder`
- **Witness(es)**:
  - `witness_lru_repr_field_order_case_basic` — max_size=42; repr must mention max_size=42 and on_miss=None
- **Source**: [#20](https://github.com/mahmoud/boltons/issues/20) — fix LRU repr reversal, fixes #20
  > ``LRI.__repr__`` (inherited by LRU) interpolated its format arguments in the wrong order: ``self.on_miss`` filled the ``max_size=`` slot and ``self.max_size`` filled the ``on_miss=`` slot. The reproduced ``repr`` was a valid Python expression that, when ``eval``'d, produced an LRI with the wrong configuration.
- **Fix commit**: `bad95b645c5fb7d14e02ad6ae479f1a05bc8185e` — fix LRU repr reversal, fixes #20
- **Invariant violated**: ``repr(LRI(max_size=n))`` contains the literal substring ``max_size=<n>`` and ``on_miss=None`` for an LRI built without an on-miss callback.
- **How the mutation triggers**: The mutation swaps the format-interpolation order back to ``(cn, self.on_miss, self.max_size, val_map)``. The repr now reports ``max_size=None`` and ``on_miss=<n>`` instead.

### 8. omd_eq_raises_on_non_iterable

- **Variant**: `omd_eq_raises_on_non_iterable_31873ae_1`
- **Location**: `boltons/dictutils.py:342` (inside `OrderedMultiDict.__eq__`)
- **Property**: `OmdEqHandlesNonIterable`
- **Witness(es)**:
  - `witness_omd_eq_handles_non_iterable_case_int` — OMD([(1,1)]) == 5 must be False, not raise
- **Source**: internal — fix a bug where __eq__ would fail with non-iterable objects of comparison
  > ``OrderedMultiDict.__eq__`` called ``len(other)`` unconditionally, so comparing against an int (or any object lacking ``__len__``) propagated TypeError. Python's data model expects ``__eq__`` to return ``NotImplemented`` or ``False`` in that situation, never raise. The fix wraps the length check in ``try/except TypeError: return False``.
- **Fix commit**: `31873aebe9df299df76053f7f2e6527ae013de9a` — fix a bug where __eq__ would fail with non-iterable objects of comparison
- **Invariant violated**: ``OMD == x`` and ``OMD != x`` return False/True (respectively) for any non-iterable ``x``, never raising.
- **How the mutation triggers**: The mutation reverts the conditional length check to a bare ``elif len(other) != len(self)``. ``len(int)`` raises TypeError, which propagates.

### 9. omd_setdefault_returns_default

- **Variant**: `omd_setdefault_returns_default_b1df971_1`
- **Location**: `boltons/dictutils.py:261` (inside `OrderedMultiDict.setdefault`)
- **Property**: `OmdSetdefaultReturnsStored`
- **Witness(es)**:
  - `witness_omd_setdefault_returns_stored_case_basic` — Stored value identity check + no-default returns None
- **Source**: internal — fix OMD.setdefault to default to None and not empty list, per documentation (and add a test to the same effect)
  > ``OrderedMultiDict.setdefault(k, v)`` did not match dict semantics: it stored ``[v]`` (or ``[]`` for the no-default case) under the key and returned the raw ``default`` argument rather than the stored value. The fix stores ``v`` (or ``None``) directly and returns ``self[k]`` so the call mirrors ``dict.setdefault``.
- **Fix commit**: `b1df97114e94f930a28b18e756c1df436ea1ac85` — fix OMD.setdefault to default to None and not empty list, per documentation (and add a test to the same effect)
- **Invariant violated**: After ``omd.setdefault(k, v)``, ``omd[k] == v`` and the call returns ``v``. For the no-default form, ``omd.setdefault(k)`` returns ``None`` and ``omd[k] is None``.
- **How the mutation triggers**: The mutation reverts to ``self[k] = [] if default is _MISSING else [default]`` and ``return default``. The stored value is wrapped in a list, and the returned value is the sentinel rather than the actual stored value.

### 10. onetoone_update_unbound_keys_vals

- **Variant**: `onetoone_update_unbound_keys_vals_6cac49c_1`
- **Location**: `boltons/dictutils.py:874` (inside `OneToOne.update`)
- **Property**: `OneToOneUpdateEmptyOk`
- **Witness(es)**:
  - `witness_one_to_one_update_empty_ok_case_basic` — Update with empty dict and empty iterable; original key intact
- **Source**: internal — fix OneToOne.update behavior with empty iterables
  > ``OneToOne.update`` only assigned ``keys_vals`` inside the ``for`` loop that hashed the new values. With an empty ``dict_or_iterable`` the loop body never ran, so ``keys_vals`` was never bound and the subsequent ``keys_vals.extend(...)`` raised UnboundLocalError. The fix initialises ``keys_vals = []`` before the conditional.
- **Fix commit**: `6cac49ce4eba506a3582e8089bcc347c6b2fa70f` — fix OneToOne.update behavior with empty iterables
- **Invariant violated**: ``OneToOne.update`` accepts an empty mapping or iterable without raising, and afterwards the prior contents of the OneToOne remain intact.
- **How the mutation triggers**: The mutation drops the ``keys_vals = []`` initialiser. With an empty dict argument, the for-loop hashing values never executes, so ``keys_vals`` is unbound when ``keys_vals.extend(kw.items())`` runs — UnboundLocalError.

### 11. remap_set_passes_pairs_to_update

- **Variant**: `remap_set_passes_pairs_to_update_f74b7e5_1`
- **Location**: `boltons/iterutils.py:1083` (inside `default_exit`)
- **Property**: `RemapPreservesSet`
- **Witness(es)**:
  - `witness_remap_preserves_set_case_three_ints` — Plain ``{1,2,3}`` round-trips through remap
- **Source**: [#84](https://github.com/mahmoud/boltons/issues/84) — fix for default remap set support, fixes #84
  > ``default_exit`` for ``Set`` containers passed ``new_items`` (a list of ``(index, value)`` 2-tuples produced earlier in ``remap``) directly to ``set.update``. ``set.update`` adds each iterable element to the set, so the resulting set was full of 2-tuples instead of the original element values. The fix passes ``vals`` — the values stripped from those 2-tuples — instead.
- **Fix commit**: `f74b7e5a7d6cc985d47540c4437a072da6803851` — fix for default remap set support, fixes #84
- **Invariant violated**: For any ``set`` or ``frozenset`` ``s``, ``remap(s) == s``.
- **How the mutation triggers**: The mutation reverts the ``set.update`` argument to ``new_items``. Each ``new_items`` element is a ``(i, v)`` tuple, so the resulting set contains those tuples instead of the bare values.

### 12. singularize_senses_to_sens

- **Variant**: `singularize_senses_to_sens_d056712_1`
- **Location**: `boltons/strutils.py:300` (inside `_IRR_S2P`)
- **Property**: `SingularizeSensesIsSense`
- **Witness(es)**:
  - `witness_singularize_senses_is_sense_case_basic` — Direct lookup against the irregular-plural table
- **Source**: internal — Fix singularize("senses") == "sens"
  > ``singularize('senses')`` produced ``'sens'`` because 'senses' was missing from the irregular plural-to-singular table. The default singularization algorithm strips a trailing 's', which is wrong here. The fix adds ``'sense': 'senses'`` to ``_IRR_S2P``.
- **Fix commit**: `d056712a4a2abcdb977a6e9a3f80bef0fcaadedd` — Fix singularize("senses") == "sens"
- **Invariant violated**: ``singularize('senses') == 'sense'``.
- **How the mutation triggers**: The mutation removes the ``'sense': 'senses'`` entry from ``_IRR_S2P``. The fallback algorithm strips the trailing 's' to give 'sens'.

### 13. stats_quantile_empty_raises

- **Variant**: `stats_quantile_empty_raises_a13bfb1_1`
- **Location**: `boltons/statsutils.py:475` (inside `Stats.get_quantile`)
- **Property**: `StatsQuantileEmptyReturnsDefault`
- **Witness(es)**:
  - `witness_stats_quantile_empty_returns_default_case_median` — q=0.5 against Stats([]) returns the default
- **Source**: internal — fix a bug with empty Stats and get_quantile
  > ``Stats([]).get_quantile(q)`` raised because the inner ``_get_quantile`` indexed into the empty sorted-data list. Other accessors on empty ``Stats`` already returned the configured ``default``; the fix extends that convention to ``get_quantile``.
- **Fix commit**: `a13bfb16fbf4f53ae23fb20cdafb69547fae8a02` — fix a bug with empty Stats and get_quantile
- **Invariant violated**: ``Stats([]).get_quantile(q)`` returns ``self.default`` for any in-range ``q``, never raising.
- **How the mutation triggers**: The mutation drops the ``elif not self.data: return self.default`` guard. The call descends into ``_get_quantile`` over empty data, which raises (IndexError or ZeroDivision).

### 14. table_to_text_row_widths

- **Variant**: `table_to_text_row_widths_0c88f25_1`
- **Location**: `boltons/tableutils.py:572` (inside `Table.to_text`)
- **Property**: `TableToTextColumnsAlign`
- **Witness(es)**:
  - `witness_table_to_text_columns_align_case_uneven` — Two-column table with widely varying cell widths
- **Source**: internal — Fix Table.to_text() sizing
  > ``Table.to_text`` measured each *row's length* (the number of cells per row) when sizing columns instead of measuring the *contents* of each column. Tables with cells whose stringified width differed from the column count produced rows whose visible widths were uneven, with long cells unpadded and short cells over-padded.
- **Fix commit**: `0c88f25323de3ff85bcca844b9ce6cd171a80392` — Fix Table.to_text() sizing
- **Invariant violated**: For each column ``j`` of ``Table.to_text(with_headers=False)``, every rendered cell width equals the maximum stringified width across all values in column ``j``.
- **How the mutation triggers**: The mutation reverts ``[len(row[idx]) for row in text_data]`` to ``[len(cur) for cur in text_data]``. The latter measures the row's element count (a constant equal to the column count) instead of cell widths, leaving long cells un-padded and short cells over-padded.
