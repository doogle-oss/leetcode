"""
Array algorithms and problems module.
"""

from .two_sum import (
    two_sum_exists,
    two_sum_indices,
    two_sum_indices_optional,
    two_sum_sorted_array,
    two_sum_sorted_array_indices
)

from .sort_colors import (
    sort_colors_dutch_flag,
    sort_colors_dutch_flag_return,
    sort_colors_counting,
    sort_colors_detailed_steps,
    validate_sorted_colors
)

from .majority_element import (
    majority_element_moores,
    majority_element_moores_with_validation,
    majority_element_hashmap,
    majority_element_sorting,
    majority_element_detailed_moores,
    find_all_majority_elements
)

__all__ = [
    # Two Sum variants
    'two_sum_exists',
    'two_sum_indices', 
    'two_sum_indices_optional',
    'two_sum_sorted_array',
    'two_sum_sorted_array_indices',
    # Sort Colors variants
    'sort_colors_dutch_flag',
    'sort_colors_dutch_flag_return',
    'sort_colors_counting',
    'sort_colors_detailed_steps',
    'validate_sorted_colors',
    # Majority Element variants
    'majority_element_moores',
    'majority_element_moores_with_validation',
    'majority_element_hashmap',
    'majority_element_sorting',
    'majority_element_detailed_moores',
    'find_all_majority_elements'
]
