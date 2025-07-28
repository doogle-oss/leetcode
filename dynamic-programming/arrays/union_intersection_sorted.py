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


if __name__ == "__main__":
    test_union_intersection()
