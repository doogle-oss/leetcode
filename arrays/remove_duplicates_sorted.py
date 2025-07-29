from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Removes duplicates from a sorted array in place.
    Returns the new length of the array after removing duplicates.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def test_remove_duplicates():
    arrs = [
        [1, 1, 2, 2, 3, 3, 4, 5, 5],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1],
        [],
        [0],
        [-3, -3, -2, -1, -1, 0, 0, 1, 2, 2],
    ]
    for arr in arrs:
        a = arr.copy()
        new_len = remove_duplicates(a)
        print(f"Original: {arr}")
        print(f"After removing duplicates: {a[:new_len]}, New length: {new_len}")
        print()


if __name__ == "__main__":
    test_remove_duplicates()
