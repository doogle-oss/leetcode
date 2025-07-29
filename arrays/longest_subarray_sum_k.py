from typing import List


def longest_subarray_with_sum_k(arr: List[int], k: int) -> int:
    """
    Returns the length of the longest subarray with sum equal to k.
    Works for arrays with positive and negative numbers.
    Time: O(n), Space: O(n)
    """
    prefix_sum = 0
    sum_indices = {0: -1}  # prefix_sum: earliest index
    max_len = 0
    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum - k in sum_indices:
            max_len = max(max_len, i - sum_indices[prefix_sum - k])
        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i
    return max_len


def longest_subarray_with_sum_k_positive_only(arr: List[int], k: int) -> int:
    """
    Returns the length of the longest subarray with sum equal to k.
    Optimized for arrays with only POSITIVE numbers using two pointers.
    Time: O(n), Space: O(1)

    Args:
        arr: List of positive integers only
        k: Target sum
    """
    if not arr or k <= 0:
        return 0

    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(arr)):
        # Expand window by adding current element
        current_sum += arr[right]

        # Shrink window from left while sum > k
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        # Check if we found target sum
        if current_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len


def test_longest_subarray_with_sum_k():
    """Test both methods with different types of arrays"""
    print("=== Testing General Method (works with negative numbers) ===")
    general_tests = [
        ([1, 2, 3, 4, 5], 9),
        ([10, 2, -2, -20, 10], -10),
        ([1, 2, 3, 7, 5], 12),
        ([1, -1, 5, -2, 3], 3),
        ([1, 2, 3], 6),
        ([1, 2, 3], 7),
        ([0, 0, 0, 0], 0),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7),
        ([], 0),
    ]
    for arr, k in general_tests:
        result = longest_subarray_with_sum_k(arr, k)
        print(f"Array: {arr}, k: {k} -> Length: {result}")

    print("\n=== Testing Two-Pointer Method (positive numbers only) ===")
    positive_tests = [
        ([1, 2, 3, 4, 5], 9),
        ([1, 2, 3, 7, 5], 12),
        ([1, 2, 3], 6),
        ([1, 2, 3], 7),
        ([3, 4, 7, 2, 1, 4, 2], 7),
        ([1, 1, 1, 1, 1], 3),
        ([5, 2, 3, 1, 4], 8),
        ([], 0),
    ]
    for arr, k in positive_tests:
        result1 = longest_subarray_with_sum_k(arr, k)
        result2 = longest_subarray_with_sum_k_positive_only(arr, k)
        match = "✓" if result1 == result2 else "✗"
        print(f"Array: {arr}, k: {k}")
        print(f"  General method: {result1}, Two-pointer: {result2} {match}")

    print("\n=== Comparison Summary ===")
    print("General Method (Prefix Sum + HashMap):")
    print("  - Time: O(n), Space: O(n)")
    print("  - Works with positive, negative, and zero")
    print("\nTwo-Pointer Method (Sliding Window):")
    print("  - Time: O(n), Space: O(1)")
    print("  - Only works with positive numbers")
    print("  - More space efficient!")


if __name__ == "__main__":
    test_longest_subarray_with_sum_k()
