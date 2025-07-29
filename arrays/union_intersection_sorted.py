from typing import List


def union_sorted(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Returns the union of two sorted arrays as a sorted list without duplicates.
    Time: O(n + m), Space: O(n + m)
    """
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1
    return result


def intersection_sorted(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Returns the intersection of two sorted arrays as a sorted list without duplicates.
    Time: O(n + m), Space: O(min(n, m))
    """
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    return result


def test_union_intersection():
    arrs = [
        ([1, 2, 2, 3, 4], [2, 2, 3, 5]),
        ([1, 3, 5], [2, 4, 6]),
        ([1, 1, 1], [1, 1, 1]),
        ([], [1, 2, 3]),
        ([1, 2, 3], []),
        ([], []),
        ([0, 2, 4, 6], [0, 2, 4, 6]),
    ]
    for arr1, arr2 in arrs:
        print(f"Array 1: {arr1}")
        print(f"Array 2: {arr2}")
        print(f"Union: {union_sorted(arr1, arr2)}")
        print(f"Intersection: {intersection_sorted(arr1, arr2)}")
        print()


def move_zeros_to_end(arr: List[int]) -> None:
    """
    Moves all zeros to the end of the array in place.
    Time: O(n), Space: O(1)
    """
    n = len(arr)
    pos = 0
    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    for i in range(pos, n):
        arr[i] = 0


def move_zeros_to_beginning(arr: List[int]) -> None:
    """
    Moves all zeros to the beginning of the array in place.
    Time: O(n), Space: O(1)
    """
    n = len(arr)
    pos = n - 1
    for i in range(n - 1, -1, -1):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos -= 1
    for i in range(pos, -1, -1):
        arr[i] = 0


def test_move_zeros():
    arrs = [
        [0, 1, 0, 3, 12],
        [1, 2, 3, 0, 0],
        [0, 0, 0, 0],
        [1, 2, 3, 4],
        [],
        [0],
        [0, 1, 0, 1, 0, 1],
    ]
    for arr in arrs:
        a = arr.copy()
        move_zeros_to_end(a)
        print(f"Move zeros to end: {arr} -> {a}")
        b = arr.copy()
        move_zeros_to_beginning(b)
        print(f"Move zeros to beginning: {arr} -> {b}")
        print()


if __name__ == "__main__":
    test_union_intersection()
    test_move_zeros()
