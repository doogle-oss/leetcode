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

from .longest_subarray_sum_k import (
    longest_subarray_with_sum_k,
    longest_subarray_with_sum_k_positive_only
)

__all__ = [
    # Two Sum variants
    'two_sum_exists',
    'two_sum_indices', 
    'two_sum_indices_optional',
    'two_sum_sorted_array',
    'two_sum_sorted_array_indices',
    # Longest subarray variants
    'longest_subarray_with_sum_k',
    'longest_subarray_with_sum_k_positive_only'
]
