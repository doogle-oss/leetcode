from typing import List


def binary_search_sorted(arr: List[int], target: int) -> int:
    """
    Performs binary search on a sorted array to find the target element.

    Time Complexity: O(log n)
        - The array is divided into half in each step.

    Space Complexity: O(1)
        - No additional space is used.

    Parameters:
    arr (List[int]): The sorted input array of integers.
    target (int): The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        print(f"finding mid: {mid}")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
            print(f"Updated left: {left}")
        else:
            right = mid - 1
            print(f"Updated right: {right}")
    return -1


def lower_bound(arr: List[int], target: int) -> int:
    """
    Finds the lower bound of the target in the sorted array.
    Lower bound is the index of the first element that is >= target.

    Parameters:
    arr (List[int]): The sorted input array of integers.
    target (int): The element to find the lower bound for.

    Returns:
    int: The index of the lower bound if found, otherwise len(arr).
    """
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr: List[int], target: int) -> int:
    """
    Finds the upper bound of the target in the sorted array.
    Upper bound is the index of the first element that is > target.

    Parameters:
    arr (List[int]): The sorted input array of integers.
    target (int): The element to find the upper bound for.

    Returns:
    int: The index of the upper bound if found, otherwise len(arr).
    """
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


# Example usage
if __name__ == "__main__":
    input_array = [1, 2, 3, 5, 7, 9, 11]
    search_target = 9  # Renamed variable to avoid conflict
    print(
        f"Index of {search_target}:", binary_search_sorted(input_array, search_target)
    )
    search_target = 5
    print(f"Lower bound of {search_target}:", lower_bound(input_array, search_target))
    print(f"Upper bound of {search_target}:", upper_bound(input_array, search_target))
