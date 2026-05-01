"""Concrete witnesses for the boltons ETNA workload.

Each ``witness_<snake>_case_<tag>`` is a no-arg function that calls
``property_<snake>`` with frozen inputs. On the base tree every witness
returns PASS; with the corresponding patch reverse-applied, the witness
returns fail(...).
"""
from ._result import PropertyResult
from . import properties


def witness_barrel_list_sort_preserves_elements_case_basic() -> PropertyResult:
    return properties.property_barrel_list_sort_preserves_elements(
        ([3, 1, 2], [6, 4, 5])
    )


def witness_table_to_text_columns_align_case_uneven() -> PropertyResult:
    return properties.property_table_to_text_columns_align(
        [("a", "BBBBBBBBBB"), ("CCCC", "d")]
    )


def witness_one_to_one_update_empty_ok_case_basic() -> PropertyResult:
    return properties.property_one_to_one_update_empty_ok(0)


def witness_bits_as_list_length_matches_case_zero_pad() -> PropertyResult:
    # val=0, n=2: buggy gives [False], correct gives [False, False].
    return properties.property_bits_as_list_length_matches((0, 2))


def witness_daterange_same_start_stop_terminates_case_zero_offset() -> PropertyResult:
    return properties.property_daterange_same_start_stop_terminates(0)


def witness_indexed_set_index_after_removals_case_pop_one() -> PropertyResult:
    # 20 items, pop index 1 — _cull keeps dead_indices since the resulting
    # dead-count (1) is below the compaction threshold (len/8 = 2.5).
    return properties.property_indexed_set_index_after_removals(
        (list(range(20)), [1])
    )


def witness_singularize_senses_is_sense_case_basic() -> PropertyResult:
    return properties.property_singularize_senses_is_sense(0)


def witness_omd_setdefault_returns_stored_case_basic() -> PropertyResult:
    return properties.property_omd_setdefault_returns_stored(42)


def witness_daterange_infinite_iterates_case_today() -> PropertyResult:
    return properties.property_daterange_infinite_iterates(0)


def witness_bytes2_human_is_repeatable_case_one_kib() -> PropertyResult:
    return properties.property_bytes2_human_is_repeatable(1024)


def witness_remap_preserves_set_case_three_ints() -> PropertyResult:
    return properties.property_remap_preserves_set([1, 2, 3])


def witness_omd_eq_handles_non_iterable_case_int() -> PropertyResult:
    return properties.property_omd_eq_handles_non_iterable(([(1, 1)], 5))


def witness_stats_quantile_empty_returns_default_case_median() -> PropertyResult:
    return properties.property_stats_quantile_empty_returns_default(50)


def witness_lru_repr_field_order_case_basic() -> PropertyResult:
    return properties.property_lru_repr_field_order(42)
