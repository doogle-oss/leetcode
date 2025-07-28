from typing import List

def bubble_sort(arr: List[int]) -> None:
    """
    Sorts the array in place using Bubble Sort.
    Time: O(n^2), Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr: List[int]) -> None:
    """
    Sorts the array in place using Insertion Sort.
    Time: O(n^2), Space: O(1)
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr: List[int]) -> None:
    """
    Sorts the array in place using Selection Sort.
    Time: O(n^2), Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def merge_sort(arr: List[int]) -> None:
    """
    Sorts the array in place using Merge Sort.
    Time: O(n log n), Space: O(n)
    """
    def merge(left: int, mid: int, right: int):
        n1 = mid - left + 1
        n2 = right - mid
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    def merge_sort_rec(left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            merge_sort_rec(left, mid)
            merge_sort_rec(mid + 1, right)
            merge(left, mid, right)
    merge_sort_rec(0, len(arr) - 1)


def test_sorts():
    arrs = [
        [5, 2, 9, 1, 5, 6],
        [3, 0, -1, 8, 7],
        [],
        [1],
        [2, 1]
    ]
    for arr in arrs:
        for sort_func in [bubble_sort, insertion_sort, selection_sort, merge_sort]:
            a = arr.copy()
            sort_func(a)
            print(f"{sort_func.__name__}: {a}")
        print()

if __name__ == "__main__":
    test_sorts()
