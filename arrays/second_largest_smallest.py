from typing import List, Optional


def second_largest(arr: List[int]) -> Optional[int]:
    """
    Returns the second largest element in the array.
    Time: O(n), Space: O(1)
    Returns None if not found.
    """
    if len(arr) < 2:
        return None
    first = second = None
    for num in arr:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    return second


def second_smallest(arr: List[int]) -> Optional[int]:
    """
    Returns the second smallest element in the array.
    Time: O(n), Space: O(1)
    Returns None if not found.
    """
    if len(arr) < 2:
        return None
    first = second = None
    for num in arr:
        if first is None or num < first:
            second = first
            first = num
        elif num != first and (second is None or num < second):
            second = num
    return second


def rotate_array(arr: List[int], k: int) -> None:
    """
    Rotates the array to the right by k positions in place.
    Time: O(n), Space: O(1)
    """
    n = len(arr)
    if n == 0 or k % n == 0:
        return
    k = k % n
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])


def test_rotate_array():
    arrs = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 5], 0),
        ([1], 3),
        ([], 1),
        ([10, 20, 30, 40], 1),
    ]
    for arr, k in arrs:
        a = arr.copy()
        rotate_array(a, k)
        print(f"Rotate {arr} by {k}: {a}")
    arrs = [
        [5, 2, 9, 1, 5, 6],
        [3, 0, -1, 8, 7],
        [1],
        [2, 2, 2],
        [10, 20],
        [-5, -2, -9, -1, -5, -6],
    ]
    for arr in arrs:
        print(f"Array: {arr}")
        print(f"Second Largest: {second_largest(arr)}")
        print(f"Second Smallest: {second_smallest(arr)}")
        print()


def test_second_largest_smallest():
    arrs = [
        [5, 2, 9, 1, 5, 6],
        [3, 0, -1, 8, 7],
        [1],
        [2, 2, 2],
        [10, 20],
        [-5, -2, -9, -1, -5, -6],
    ]
    for arr in arrs:
        print(f"Array: {arr}")
        print(f"Second Largest: {second_largest(arr)}")
        print(f"Second Smallest: {second_smallest(arr)}")
        print()


if __name__ == "__main__":
    test_second_largest_smallest()
    test_rotate_array()
