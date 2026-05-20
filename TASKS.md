# boltons — ETNA Tasks

Total tasks: 28

## Task Index

| Task | Variant | Framework | Property | Witness |
|------|---------|-----------|----------|---------|
| 001 | `barrellist_sort_drops_lists_b8855d7_1` | hypothesis | `BarrelListSortPreservesElements` | `witness_barrel_list_sort_preserves_elements_case_basic` |
| 002 | `barrellist_sort_drops_lists_b8855d7_1` | crosshair | `BarrelListSortPreservesElements` | `witness_barrel_list_sort_preserves_elements_case_basic` |
| 003 | `bits_as_list_truncates_zero_pad_40a7b47_1` | hypothesis | `BitsAsListLengthMatches` | `witness_bits_as_list_length_matches_case_zero_pad` |
| 004 | `bits_as_list_truncates_zero_pad_40a7b47_1` | crosshair | `BitsAsListLengthMatches` | `witness_bits_as_list_length_matches_case_zero_pad` |
| 005 | `bytes2human_size_ranges_consumed_0082e13_1` | hypothesis | `Bytes2HumanIsRepeatable` | `witness_bytes2_human_is_repeatable_case_one_kib` |
| 006 | `bytes2human_size_ranges_consumed_0082e13_1` | crosshair | `Bytes2HumanIsRepeatable` | `witness_bytes2_human_is_repeatable_case_one_kib` |
| 007 | `daterange_finished_arity_mismatch_139d5dc_1` | hypothesis | `DaterangeInfiniteIterates` | `witness_daterange_infinite_iterates_case_today` |
| 008 | `daterange_finished_arity_mismatch_139d5dc_1` | crosshair | `DaterangeInfiniteIterates` | `witness_daterange_infinite_iterates_case_today` |
| 009 | `daterange_inclusive_same_start_stop_93185b2_1` | hypothesis | `DaterangeSameStartStopTerminates` | `witness_daterange_same_start_stop_terminates_case_zero_offset` |
| 010 | `daterange_inclusive_same_start_stop_93185b2_1` | crosshair | `DaterangeSameStartStopTerminates` | `witness_daterange_same_start_stop_terminates_case_zero_offset` |
| 011 | `indexed_set_index_ignores_dead_4457dec_1` | hypothesis | `IndexedSetIndexAfterRemovals` | `witness_indexed_set_index_after_removals_case_pop_one` |
| 012 | `indexed_set_index_ignores_dead_4457dec_1` | crosshair | `IndexedSetIndexAfterRemovals` | `witness_indexed_set_index_after_removals_case_pop_one` |
| 013 | `lru_repr_swaps_max_size_on_miss_bad95b6_1` | hypothesis | `LruReprFieldOrder` | `witness_lru_repr_field_order_case_basic` |
| 014 | `lru_repr_swaps_max_size_on_miss_bad95b6_1` | crosshair | `LruReprFieldOrder` | `witness_lru_repr_field_order_case_basic` |
| 015 | `omd_eq_raises_on_non_iterable_31873ae_1` | hypothesis | `OmdEqHandlesNonIterable` | `witness_omd_eq_handles_non_iterable_case_int` |
| 016 | `omd_eq_raises_on_non_iterable_31873ae_1` | crosshair | `OmdEqHandlesNonIterable` | `witness_omd_eq_handles_non_iterable_case_int` |
| 017 | `omd_setdefault_returns_default_b1df971_1` | hypothesis | `OmdSetdefaultReturnsStored` | `witness_omd_setdefault_returns_stored_case_basic` |
| 018 | `omd_setdefault_returns_default_b1df971_1` | crosshair | `OmdSetdefaultReturnsStored` | `witness_omd_setdefault_returns_stored_case_basic` |
| 019 | `onetoone_update_unbound_keys_vals_6cac49c_1` | hypothesis | `OneToOneUpdateEmptyOk` | `witness_one_to_one_update_empty_ok_case_basic` |
| 020 | `onetoone_update_unbound_keys_vals_6cac49c_1` | crosshair | `OneToOneUpdateEmptyOk` | `witness_one_to_one_update_empty_ok_case_basic` |
| 021 | `remap_set_passes_pairs_to_update_f74b7e5_1` | hypothesis | `RemapPreservesSet` | `witness_remap_preserves_set_case_three_ints` |
| 022 | `remap_set_passes_pairs_to_update_f74b7e5_1` | crosshair | `RemapPreservesSet` | `witness_remap_preserves_set_case_three_ints` |
| 023 | `singularize_senses_to_sens_d056712_1` | hypothesis | `SingularizeSensesIsSense` | `witness_singularize_senses_is_sense_case_basic` |
| 024 | `singularize_senses_to_sens_d056712_1` | crosshair | `SingularizeSensesIsSense` | `witness_singularize_senses_is_sense_case_basic` |
| 025 | `stats_quantile_empty_raises_a13bfb1_1` | hypothesis | `StatsQuantileEmptyReturnsDefault` | `witness_stats_quantile_empty_returns_default_case_median` |
| 026 | `stats_quantile_empty_raises_a13bfb1_1` | crosshair | `StatsQuantileEmptyReturnsDefault` | `witness_stats_quantile_empty_returns_default_case_median` |
| 027 | `table_to_text_row_widths_0c88f25_1` | hypothesis | `TableToTextColumnsAlign` | `witness_table_to_text_columns_align_case_uneven` |
| 028 | `table_to_text_row_widths_0c88f25_1` | crosshair | `TableToTextColumnsAlign` | `witness_table_to_text_columns_align_case_uneven` |

## Witness Catalog

- `witness_barrel_list_sort_preserves_elements_case_basic` — Two internal lists; sort must not raise and must preserve elements
- `witness_bits_as_list_length_matches_case_zero_pad` — Bits(0, 2): expected [False, False]; bug returns [False]
- `witness_bytes2_human_is_repeatable_case_one_kib` — Two consecutive 1024-byte calls; the second observes the drained iterator
- `witness_daterange_infinite_iterates_case_today` — Three pulls verify both the first and the inner-loop termination calls
- `witness_daterange_same_start_stop_terminates_case_zero_offset` — Bounded islice keeps the test from hanging on the infinite branch
- `witness_indexed_set_index_after_removals_case_pop_one` — 20-item set; popping a middle index leaves dead_indices populated
- `witness_lru_repr_field_order_case_basic` — max_size=42; repr must mention max_size=42 and on_miss=None
- `witness_omd_eq_handles_non_iterable_case_int` — OMD([(1,1)]) == 5 must be False, not raise
- `witness_omd_setdefault_returns_stored_case_basic` — Stored value identity check + no-default returns None
- `witness_one_to_one_update_empty_ok_case_basic` — Update with empty dict and empty iterable; original key intact
- `witness_remap_preserves_set_case_three_ints` — Plain ``{1,2,3}`` round-trips through remap
- `witness_singularize_senses_is_sense_case_basic` — Direct lookup against the irregular-plural table
- `witness_stats_quantile_empty_returns_default_case_median` — q=0.5 against Stats([]) returns the default
- `witness_table_to_text_columns_align_case_uneven` — Two-column table with widely varying cell widths
