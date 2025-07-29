from typing import List, Optional


def majority_element_moores(arr: List[int]) -> int:
    """
    Find the majority element using Moore's Voting Algorithm.
    Assumes majority element always exists (appears > n/2 times).
    Time: O(n), Space: O(1)
    
    Algorithm:
    1. Find candidate: Use voting to find potential majority element
    2. Since majority is guaranteed, candidate is the answer
    
    Args:
        arr: List of integers with guaranteed majority element
        
    Returns:
        int: The majority element
    """
    candidate = None
    count = 0
    
    # Phase 1: Find candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate


def majority_element_moores_with_validation(arr: List[int]) -> Optional[int]:
    """
    Find the majority element using Moore's Voting Algorithm with validation.
    Does not assume majority element exists.
    Time: O(n), Space: O(1)
    
    Args:
        arr: List of integers
        
    Returns:
        Optional[int]: The majority element if exists, None otherwise
    """
    if not arr:
        return None
    
    candidate = None
    count = 0
    
    # Phase 1: Find candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Phase 2: Validate candidate
    if candidate is not None:
        actual_count = sum(1 for num in arr if num == candidate)
        if actual_count > len(arr) // 2:
            return candidate
    
    return None


def majority_element_hashmap(arr: List[int]) -> Optional[int]:
    """
    Find majority element using hashmap (brute force approach).
    Time: O(n), Space: O(n)
    
    Args:
        arr: List of integers
        
    Returns:
        Optional[int]: The majority element if exists, None otherwise
    """
    if not arr:
        return None
    
    count_map = {}
    majority_threshold = len(arr) // 2
    
    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1
        if count_map[num] > majority_threshold:
            return num
    
    return None


def majority_element_sorting(arr: List[int]) -> Optional[int]:
    """
    Find majority element using sorting approach.
    Time: O(n log n), Space: O(1) if in-place sort
    
    Logic: If majority element exists, it must be at index n//2 after sorting.
    
    Args:
        arr: List of integers
        
    Returns:
        Optional[int]: The majority element if exists, None otherwise
    """
    if not arr:
        return None
    
    sorted_arr = sorted(arr)
    candidate = sorted_arr[len(arr) // 2]
    
    # Validate candidate
    count = sum(1 for num in arr if num == candidate)
    if count > len(arr) // 2:
        return candidate
    
    return None


def majority_element_detailed_moores(arr: List[int]) -> int:
    """
    Moore's Voting Algorithm with detailed step-by-step visualization.
    Assumes majority element exists.
    Time: O(n), Space: O(1)
    
    Args:
        arr: List of integers with guaranteed majority element
        
    Returns:
        int: The majority element
    """
    print(f"Finding majority element in: {arr}")
    print("Using Moore's Voting Algorithm\n")
    
    candidate = None
    count = 0
    
    print("Phase 1: Finding candidate")
    print("-" * 30)
    
    for i, num in enumerate(arr):
        print(f"Step {i+1}: num = {num}")
        
        if count == 0:
            candidate = num
            count = 1
            print(f"  Count is 0, set candidate = {candidate}, count = {count}")
        elif num == candidate:
            count += 1
            print(f"  num == candidate, increment count = {count}")
        else:
            count -= 1
            print(f"  num != candidate, decrement count = {count}")
        
        print(f"  Current state: candidate = {candidate}, count = {count}\n")
    
    print(f"Final candidate: {candidate}")
    print(f"Verification: This is the majority element (guaranteed by problem)")
    
    return candidate


def find_all_majority_elements(arr: List[int], threshold_fraction: float = 0.5) -> List[int]:
    """
    Find all elements that appear more than threshold_fraction of the time.
    Generalized version for different thresholds.
    Time: O(n), Space: O(n)
    
    Args:
        arr: List of integers
        threshold_fraction: Minimum fraction for majority (default 0.5 for > n/2)
        
    Returns:
        List[int]: All majority elements
    """
    if not arr:
        return []
    
    count_map = {}
    threshold = len(arr) * threshold_fraction
    
    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1
    
    return [num for num, count in count_map.items() if count > threshold]


def test_majority_element():
    """Test all majority element finding methods"""
    print("=== Testing Majority Element Algorithms ===\n")
    
    test_cases = [
        ([3, 2, 3], "3 appears 2/3 times"),
        ([2, 2, 1, 1, 1, 2, 2], "2 appears 4/7 times"),
        ([1], "Single element"),
        ([1, 1, 1, 1, 2, 3, 4], "1 appears 4/7 times"),
        ([1, 2, 3, 4, 5], "No majority element"),
        ([1, 1, 2, 2, 3, 3], "No majority element"),
        ([5, 5, 5, 5, 1, 2, 3], "5 appears 4/7 times"),
        ([1, 2, 1, 2, 1], "1 appears 3/5 times"),
    ]
    
    print("1. MOORE'S VOTING ALGORITHM (Optimized - assumes majority exists):")
    print("-" * 70)
    guaranteed_cases = [
        ([3, 2, 3], "3 appears 2/3 times"),
        ([2, 2, 1, 1, 1, 2, 2], "2 appears 4/7 times"),
        ([1], "Single element"),
        ([1, 1, 1, 1, 2, 3, 4], "1 appears 4/7 times"),
        ([5, 5, 5, 5, 1, 2, 3], "5 appears 4/7 times"),
        ([1, 2, 1, 2, 1], "1 appears 3/5 times"),
    ]
    
    for arr, description in guaranteed_cases:
        result = majority_element_moores(arr)
        print(f"Array: {arr}")
        print(f"Description: {description}")
        print(f"Majority element: {result}\n")
    
    print("2. MOORE'S VOTING WITH VALIDATION (handles no majority case):")
    print("-" * 65)
    for arr, description in test_cases:
        result = majority_element_moores_with_validation(arr)
        print(f"Array: {arr}")
        print(f"Description: {description}")
        print(f"Majority element: {result}\n")
    
    print("3. HASHMAP APPROACH:")
    print("-" * 20)
    for arr, description in test_cases:
        result = majority_element_hashmap(arr)
        print(f"Array: {arr} -> Majority: {result}")
    
    print("\n4. SORTING APPROACH:")
    print("-" * 20)
    for arr, description in test_cases:
        result = majority_element_sorting(arr)
        print(f"Array: {arr} -> Majority: {result}")
    
    print("\n5. DETAILED MOORE'S ALGORITHM (step-by-step):")
    print("-" * 50)
    example = [2, 2, 1, 1, 1, 2, 2]
    print(f"Demonstrating with: {example}")
    print("=" * 60)
    majority_element_detailed_moores(example)
    
    print("\n6. GENERALIZED MAJORITY (different thresholds):")
    print("-" * 50)
    test_array = [1, 1, 1, 2, 2, 3]
    thresholds = [0.3, 0.4, 0.5]
    for threshold in thresholds:
        result = find_all_majority_elements(test_array, threshold)
        print(f"Array: {test_array}, threshold > {threshold*100}%: {result}")
    
    print("\n=== Algorithm Comparison ===")
    print("1. Moore's Voting Algorithm:")
    print("   - Time: O(n), Space: O(1)")
    print("   - OPTIMAL solution")
    print("   - Single pass through array")
    print("   - Requires validation if majority not guaranteed")
    print("\n2. HashMap Approach:")
    print("   - Time: O(n), Space: O(n)")
    print("   - Easy to understand")
    print("   - Good for multiple majority elements")
    print("\n3. Sorting Approach:")
    print("   - Time: O(n log n), Space: O(1)")
    print("   - Less efficient but intuitive")
    print("   - Majority element at middle position")
    
    print("\n=== Moore's Algorithm Explanation ===")
    print("Key Insight:")
    print("- If an element appears > n/2 times, it will survive the 'voting'")
    print("- Each occurrence of majority element gets +1 vote")
    print("- Each occurrence of other elements gets -1 vote")
    print("- Majority element will have net positive votes")
    print("\nWhy it works:")
    print("- Majority element appears more than all others combined")
    print("- Even if we 'cancel out' with different elements, majority survives")


def benchmark_majority_algorithms():
    """Compare performance of different algorithms"""
    import time
    
    # Create test array with guaranteed majority
    test_size = 100000
    majority_element = 42
    test_array = [majority_element] * (test_size // 2 + 1)  # Majority
    test_array.extend([i for i in range(test_size // 2 - 1)])  # Minorities
    
    print(f"\n=== Performance Benchmark ===")
    print(f"Array size: {len(test_array)}")
    print(f"Majority element: {majority_element} (appears {test_array.count(majority_element)} times)")
    
    # Test Moore's algorithm
    start = time.time()
    result1 = majority_element_moores(test_array)
    moores_time = time.time() - start
    
    # Test HashMap algorithm
    start = time.time()
    result2 = majority_element_hashmap(test_array)
    hashmap_time = time.time() - start
    
    print(f"\nResults:")
    print(f"Moore's Algorithm: {result1} (Time: {moores_time:.6f}s)")
    print(f"HashMap Algorithm: {result2} (Time: {hashmap_time:.6f}s)")
    print(f"Moore's is {hashmap_time/moores_time:.2f}x faster!")


if __name__ == "__main__":
    test_majority_element()
    benchmark_majority_algorithms()
