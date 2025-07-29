from typing import List


def longest_subarray_with_sum_k(arr: List[int], k: int) -> int:
    """
    Returns the length of the longest subarray with sum equal to k.
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


def test_longest_subarray_with_sum_k():
    tests = [
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
    for arr, k in tests:
        print(f"Array: {arr}, k: {k}")
        print(f"Longest subarray length: {longest_subarray_with_sum_k(arr, k)}")
        print()


if __name__ == "__main__":
    test_longest_subarray_with_sum_k()
