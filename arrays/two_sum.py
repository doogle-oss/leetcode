from typing import List, Tuple, Optional


def two_sum_exists(arr: List[int], target: int) -> bool:
    """
    Check if there exist two numbers in the array that sum to target.
    Time: O(n), Space: O(n)
    
    Args:
        arr: List of integers
        target: Target sum
        
    Returns:
        bool: True if two numbers exist that sum to target, False otherwise
    """
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False


def two_sum_indices(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Find indices of two numbers that sum to target.
    Assumes exactly one solution exists (guaranteed).
    Time: O(n), Space: O(n)
    
    Args:
        arr: List of integers
        target: Target sum
        
    Returns:
        Tuple[int, int]: Indices of the two numbers that sum to target
        
    Raises:
        ValueError: If no solution exists (violates guarantee)
    """
    num_to_index = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], i)
        num_to_index[num] = i
    
    # This should never happen if guarantee is met
    raise ValueError("No two sum solution found - guarantee violated")


def two_sum_indices_optional(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find indices of two numbers that sum to target.
    Returns None if no solution exists.
    Time: O(n), Space: O(n)
    
    Args:
        arr: List of integers
        target: Target sum
        
    Returns:
        Optional[Tuple[int, int]]: Indices of two numbers or None if not found
    """
    num_to_index = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], i)
        num_to_index[num] = i
    
    return None


def two_sum_sorted_array(arr: List[int], target: int) -> bool:
    """
    Two sum for sorted array using two pointers.
    More space efficient for sorted arrays.
    Time: O(n), Space: O(1)
    
    Args:
        arr: Sorted list of integers
        target: Target sum
        
    Returns:
        bool: True if two numbers exist that sum to target
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return False


def two_sum_sorted_array_indices(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Two sum for sorted array returning indices.
    Time: O(n), Space: O(1)
    
    Args:
        arr: Sorted list of integers
        target: Target sum
        
    Returns:
        Optional[Tuple[int, int]]: Indices of two numbers or None if not found
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None


def test_two_sum():
    """Test all two sum variants"""
    print("=== Testing Two Sum Variants ===\n")
    
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 8),
        ([1, 2, 3, 4, 5], 10),
        ([-1, 0, 1, 2, -1, -4], -2),
        ([], 0),
        ([1], 1),
        ([1, 2], 4),
    ]
    
    print("1. EXISTS CHECK (True/False):")
    print("-" * 30)
    for arr, target in test_cases:
        exists = two_sum_exists(arr, target)
        print(f"Array: {arr}, Target: {target} -> Exists: {exists}")
    
    print("\n2. INDICES (Guaranteed Solution):")
    print("-" * 35)
    guaranteed_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 8),
        ([-1, 0, 1, 2, -1, -4], -2),
    ]
    
    for arr, target in guaranteed_cases:
        try:
            indices = two_sum_indices(arr, target)
            values = (arr[indices[0]], arr[indices[1]])
            print(f"Array: {arr}, Target: {target}")
            print(f"  Indices: {indices}, Values: {values}, Sum: {sum(values)}")
        except ValueError as e:
            print(f"Array: {arr}, Target: {target} -> {e}")
    
    print("\n3. INDICES (Optional - handles no solution):")
    print("-" * 45)
    for arr, target in test_cases:
        indices = two_sum_indices_optional(arr, target)
        if indices:
            values = (arr[indices[0]], arr[indices[1]])
            print(f"Array: {arr}, Target: {target}")
            print(f"  Indices: {indices}, Values: {values}")
        else:
            print(f"Array: {arr}, Target: {target} -> No solution")
    
    print("\n4. SORTED ARRAY (Two Pointers):")
    print("-" * 35)
    sorted_cases = [
        ([1, 2, 3, 4, 5], 8),
        ([2, 7, 11, 15], 9),
        ([-4, -1, -1, 0, 1, 2], -2),
        ([1, 2, 3, 4, 5], 10),
    ]
    
    for arr, target in sorted_cases:
        exists = two_sum_sorted_array(arr, target)
        indices = two_sum_sorted_array_indices(arr, target)
        print(f"Sorted Array: {arr}, Target: {target}")
        print(f"  Exists: {exists}, Indices: {indices}")
    
    print("\n=== Algorithm Comparison ===")
    print("1. Hash Map Approach:")
    print("   - Time: O(n), Space: O(n)")
    print("   - Works with unsorted arrays")
    print("   - Best for general case")
    print("\n2. Two Pointers (Sorted Array):")
    print("   - Time: O(n), Space: O(1)")
    print("   - Requires sorted array")
    print("   - More space efficient")
    print("   - If array needs sorting: O(n log n) time")


if __name__ == "__main__":
    test_two_sum()
