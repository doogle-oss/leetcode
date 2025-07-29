from calendar import c
from typing import List


def sort_colors_dutch_flag(arr: List[int]) -> None:
    """
    Sort array containing only 0s, 1s, and 2s using Dutch National Flag algorithm.
    Modifies the array in-place.
    Time: O(n), Space: O(1)

    Algorithm:
    - low: boundary for 0s (everything before low is 0)
    - mid: current element being processed
    - high: boundary for 2s (everything after high is 2)

    Args:
        arr: List containing only 0, 1, 2
    """
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            # Swap with low and move both pointers
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # 1 is in correct position, just move mid
            mid += 1
        else:  # arr[mid] == 2
            # Swap with high, move high pointer, don't move mid yet
            # (we need to check the swapped element)
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # Don't increment mid here because we need to check the swapped element


def sort_colors_dutch_flag_return(arr: List[int]) -> List[int]:
    """
    Sort array containing only 0s, 1s, and 2s using Dutch National Flag algorithm.
    Returns a new sorted array without modifying the original.
    Time: O(n), Space: O(n)

    Args:
        arr: List containing only 0, 1, 2

    Returns:
        List[int]: New sorted array
    """
    result = arr.copy()
    sort_colors_dutch_flag(result)
    return result


def sort_colors_counting(arr: List[int]) -> None:
    """
    Sort array using counting approach (alternative solution).
    Time: O(n), Space: O(1)

    Args:
        arr: List containing only 0, 1, 2
    """
    counter = [0, 0, 0]  # [count_0, count_1, count_2]

    # Count occurrences
    for num in arr:
        if num == 0:
            counter[0] += 1
        elif num == 1:
            counter[1] += 1
        else:  # num == 2
            counter[2] += 1

    # Fill 0s
    for idx in range(len(arr)):
        if idx < count_0:
            arr[idx] = 0
        elif idx < count_0 + count_1:
            arr[idx] = 1
        else:
            arr[idx] = 2


def sort_colors_detailed_steps(arr: List[int]) -> List[int]:
    """
    Sort array with detailed step-by-step visualization of Dutch Flag algorithm.
    Returns sorted array and prints each step.
    Time: O(n), Space: O(n)

    Args:
        arr: List containing only 0, 1, 2

    Returns:
        List[int]: Sorted array
    """
    result = arr.copy()
    low = 0
    mid = 0
    high = len(result) - 1
    step = 1

    print(f"Initial: {result}")
    print(f"low={low}, mid={mid}, high={high}\n")

    while mid <= high:
        print(f"Step {step}: arr[mid={mid}] = {result[mid]}")

        if result[mid] == 0:
            print(f"  Found 0: swap arr[{low}] and arr[{mid}]")
            result[low], result[mid] = result[mid], result[low]
            print(f"  After swap: {result}")
            low += 1
            mid += 1
            print(f"  low={low}, mid={mid}, high={high}")

        elif result[mid] == 1:
            print(f"  Found 1: already in correct region, move mid")
            mid += 1
            print(f"  low={low}, mid={mid}, high={high}")

        else:  # result[mid] == 2
            print(f"  Found 2: swap arr[{mid}] and arr[{high}]")
            result[mid], result[high] = result[high], result[mid]
            print(f"  After swap: {result}")
            high -= 1
            print(f"  low={low}, mid={mid}, high={high}")
            print(f"  (Don't increment mid - need to check swapped element)")

        print()
        step += 1

    print(f"Final sorted: {result}")
    return result


def test_sort_colors():
    """Test all sorting variants with comprehensive test cases"""
    print("=== Testing Sort Colors (0, 1, 2) ===\n")

    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0, 1, 2],
        [2, 1, 0],
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2],
        [1, 0, 2, 1, 0, 2, 1, 0],
        [2, 1, 2, 0, 0, 1],
        [0],
        [1],
        [2],
        [],
    ]

    print("1. DUTCH FLAG ALGORITHM (In-place):")
    print("-" * 40)
    for i, original in enumerate(test_cases):
        arr_copy = original.copy()
        sort_colors_dutch_flag(arr_copy)
        print(f"Test {i+1}: {original} -> {arr_copy}")

    print("\n2. DUTCH FLAG (Return new array):")
    print("-" * 40)
    for i, original in enumerate(test_cases):
        sorted_arr = sort_colors_dutch_flag_return(original)
        print(f"Test {i+1}: {original} -> {sorted_arr}")

    print("\n3. COUNTING APPROACH:")
    print("-" * 25)
    for i, original in enumerate(test_cases):
        arr_copy = original.copy()
        sort_colors_counting(arr_copy)
        print(f"Test {i+1}: {original} -> {arr_copy}")

    print("\n4. DETAILED STEP-BY-STEP (Dutch Flag):")
    print("-" * 45)
    example = [2, 0, 2, 1, 1, 0]
    print(f"Demonstrating with: {example}")
    print("=" * 50)
    sort_colors_detailed_steps(example)

    print("\n=== Algorithm Comparison ===")
    print("1. Dutch National Flag Algorithm:")
    print("   - Time: O(n), Space: O(1)")
    print("   - Single pass through array")
    print("   - In-place sorting")
    print("   - Optimal for this specific problem")
    print("   - Uses three pointers: low, mid, high")
    print("\n2. Counting Sort:")
    print("   - Time: O(n), Space: O(1)")
    print("   - Two passes: count then fill")
    print("   - Simpler to understand")
    print("   - Good for interview explanation")

    print("\n=== Dutch Flag Algorithm Explanation ===")
    print("Invariants maintained:")
    print("- arr[0...low-1] contains only 0s")
    print("- arr[low...mid-1] contains only 1s")
    print("- arr[high+1...n-1] contains only 2s")
    print("- arr[mid...high] is unknown region")
    print("\nProcess:")
    print("- If arr[mid] == 0: swap with low, increment both low and mid")
    print("- If arr[mid] == 1: just increment mid (already correct)")
    print("- If arr[mid] == 2: swap with high, decrement high (don't increment mid)")


def validate_sorted_colors(arr: List[int]) -> bool:
    """
    Validate if array is properly sorted with 0s, 1s, 2s.

    Args:
        arr: Array to validate

    Returns:
        bool: True if properly sorted
    """
    if not arr:
        return True

    # Check if all elements are 0, 1, or 2
    if not all(x in [0, 1, 2] for x in arr):
        return False

    # Check if sorted: all 0s, then all 1s, then all 2s
    prev = -1
    for num in arr:
        if num < prev:
            return False
        prev = num

    return True


if __name__ == "__main__":
    test_sort_colors()

    # Additional validation test
    print("\n=== Validation Test ===")
    test_arrays = [[2, 0, 2, 1, 1, 0], [0, 1, 2], [2, 1, 0]]

    for original in test_arrays:
        sorted_arr = sort_colors_dutch_flag_return(original)
        is_valid = validate_sorted_colors(sorted_arr)
        print(f"{original} -> {sorted_arr} (Valid: {is_valid})")
