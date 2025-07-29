from typing import List, Optional


def max_subarray_sum_kadane(arr: List[int]) -> int:
    """
    Find the maximum subarray sum using Kadane's Algorithm.
    Time: O(n), Space: O(1)
    Handles negative numbers as well.

    Args:
        arr: List of integers
    Returns:
        int: Maximum subarray sum
    """
    if not arr:
        return 0
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def max_subarray_sum_kadane_with_indices(
    arr: List[int],
) -> Optional[tuple[int, int, int]]:
    """
    Kadane's Algorithm with indices of the subarray.
    Returns (max_sum, start_index, end_index) or None if arr is empty.
    Time: O(n), Space: O(1)

    Args:
        arr: List of integers
    Returns:
        Optional[tuple[int, int, int]]: (max_sum, start, end) or None
    """
    if not arr:
        return None
    max_sum = current_sum = arr[0]
    start = end = s = 0
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
    return (max_sum, start, end)


def max_subarray_sum_kadane_detailed(arr: List[int]) -> int:
    """
    Kadane's Algorithm with step-by-step printout.
    Time: O(n), Space: O(1)

    Args:
        arr: List of integers
    Returns:
        int: Maximum subarray sum
    """
    if not arr:
        print("Empty array. Max sum is 0.")
        return 0
    max_sum = current_sum = arr[0]
    print(f"Initial: max_sum = {max_sum}, current_sum = {current_sum}")
    for i, num in enumerate(arr[1:], 1):
        print(f"Step {i}: num = {num}")
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        print(f"  current_sum = {current_sum}, max_sum = {max_sum}")
    print(f"Final max subarray sum: {max_sum}")
    return max_sum


def test_kadane():
    print("=== Testing Kadane's Algorithm ===\n")
    test_cases = [
        [1, -2, 3, 4, -1, 2, 1, -5, 4],
        [-2, -3, 4, -1, -2, 1, 5, -3],
        [5, 4, -1, 7, 8],
        [-1, -2, -3, -4],
        [1],
        [],
        [0, 0, 0, 0],
        [2, -1, 2, 3, 4, -5],
    ]
    for arr in test_cases:
        result = max_subarray_sum_kadane(arr)
        indices = max_subarray_sum_kadane_with_indices(arr)
        print(f"Array: {arr}")
        print(f"  Max subarray sum: {result}")
        if indices:
            print(f"  (sum, start, end): {indices}")
        print()
    print("\n=== Detailed Example ===")
    example = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    max_subarray_sum_kadane_detailed(example)


if __name__ == "__main__":
    test_kadane()
