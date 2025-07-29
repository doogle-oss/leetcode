from typing import List


def missing_number_sum(nums: List[int]) -> int:
    """
    Finds the missing number in the range [0, n] using sum formula.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def missing_number_xor(nums: List[int]) -> int:
    n = len(nums)
    xor = 0
    for i in range(n):
        xor ^= i ^ nums[i]
    xor ^= n
    return xor


def test_missing_number():
    arrs = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
        [0],
        [1],
        [0, 2],
        [2, 1],
        [],
    ]
    for arr in arrs:
        print(f"Array: {arr}")
        print(f"Missing (sum): {missing_number_sum(arr)}")
        print(f"Missing (xor): {missing_number_xor(arr)}")
        print()


if __name__ == "__main__":
    test_missing_number()
