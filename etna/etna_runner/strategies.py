"""Hypothesis strategies for the boltons ETNA workload.

CrossHair-compatible: stick to ``st.integers``, ``st.text``, ``st.lists``,
``st.tuples``, ``st.booleans`` — no custom ``@composite`` strategies.
"""
from hypothesis import strategies as st


_INT = st.integers(min_value=-100, max_value=100)
_SMALL_NAT = st.integers(min_value=0, max_value=64)
_TEXT_PRINTABLE = st.text(
    alphabet=st.characters(min_codepoint=32, max_codepoint=126,
                           blacklist_characters="|"),
    max_size=8,
)


def strategy_barrel_list_sort_preserves_elements():
    return st.tuples(
        st.lists(_INT, max_size=8),
        st.lists(_INT, max_size=8),
    )


def strategy_table_to_text_columns_align():
    return st.lists(
        st.tuples(_TEXT_PRINTABLE, _TEXT_PRINTABLE),
        max_size=4,
    )


def strategy_one_to_one_update_empty_ok():
    return _INT


def strategy_bits_as_list_length_matches():
    return st.tuples(
        st.integers(min_value=0, max_value=255),
        st.integers(min_value=1, max_value=8),
    )


def strategy_daterange_same_start_stop_terminates():
    return st.integers(min_value=-365, max_value=365)


def strategy_indexed_set_index_after_removals():
    # min_size=20 keeps dead_count below the IndexedSet compaction threshold
    # so the bug surfaces (small sets are compacted eagerly and the bug is
    # hidden by item_list rebuild).
    return st.tuples(
        st.lists(_INT, min_size=20, max_size=24, unique=True),
        st.lists(_SMALL_NAT, min_size=1, max_size=2),
    )


def strategy_singularize_senses_is_sense():
    return st.integers(min_value=0, max_value=10)


def strategy_omd_setdefault_returns_stored():
    return _INT


def strategy_daterange_infinite_iterates():
    return st.integers(min_value=-365, max_value=365)


def strategy_bytes2_human_is_repeatable():
    return st.integers(min_value=0, max_value=1024 * 1024)


def strategy_remap_preserves_set():
    return st.lists(_INT, max_size=6)


def strategy_omd_eq_handles_non_iterable():
    return st.tuples(
        st.lists(st.tuples(_INT, _INT), max_size=4),
        _INT,
    )


def strategy_stats_quantile_empty_returns_default():
    return st.integers(min_value=0, max_value=100)


def strategy_lru_repr_field_order():
    return st.integers(min_value=1, max_value=1024)
