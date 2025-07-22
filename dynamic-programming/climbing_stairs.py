def frog_jump_min_energy(heights):
    """
    Space-optimized frog jump solution
    Time Complexity: O(n)
    Space Complexity: O(1) - only using two variables instead of full DP array
    """
    n = len(heights)
    if n == 0:
        return 0
    if n == 1:
        return 0
    
    # Only keep track of previous two values instead of entire DP array
    prev2 = 0  # dp[i-2]: minimum energy to reach step i-2
    prev1 = 0  # dp[i-1]: minimum energy to reach step i-1
    
    for i in range(1, n):
        one_step = prev1 + abs(heights[i] - heights[i-1])
        two_step = prev2 + abs(heights[i] - heights[i-2]) if i > 1 else float('inf')
        
        current = min(one_step, two_step)
        
        # Update previous values for next iteration
        prev2 = prev1
        prev1 = current
    
    return prev1


def frog_jump_min_energy_original(heights):
    """
    Original O(n) space solution for comparison
    Time Complexity: O(n)
    Space Complexity: O(n) - uses full DP array
    """
    n = len(heights)
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        one_step = dp[i-1] + abs(heights[i] - heights[i-1])
        two_step = dp[i-2] + abs(heights[i] - heights[i-2]) if i > 1 else float('inf')
        dp[i] = min(one_step, two_step)
    return dp[-1]


def test_frog_jump_solutions():
    """Test both original and space-optimized solutions"""
    
    test_cases = [
        {
            "heights": [10, 30, 40, 20],
            "expected": 30,
            "description": "Basic example - optimal path: 0→1→3 (cost: 20+10=30)"
        },
        {
            "heights": [10],
            "expected": 0,
            "description": "Single step - no movement needed"
        },
        {
            "heights": [10, 20],
            "expected": 10,
            "description": "Two steps - only one jump possible"
        },
        {
            "heights": [10, 20, 30],
            "expected": 20,
            "description": "Three steps - can jump directly from 0 to 2"
        },
        {
            "heights": [10, 50, 10, 20],
            "expected": 20,
            "description": "Skip high middle step - path: 0→2→3"
        },
        {
            "heights": [7, 4, 4, 2, 0, 10, 3, 3, 1, 3],
            "expected": 7,
            "description": "Complex case with multiple optimal paths"
        }
    ]
    
    print("Testing Frog Jump Solutions:")
    print("=" * 50)
    
    for i, test in enumerate(test_cases, 1):
        heights = test["heights"]
        expected = test["expected"]
        
        # Test space-optimized solution
        result_optimized = frog_jump_min_energy(heights)
        
        # Test original solution
        result_original = frog_jump_min_energy_original(heights)
        
        print(f"Test {i}: {test['description']}")
        print(f"  Heights: {heights}")
        print(f"  Expected: {expected}")
        print(f"  Space-Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}")
        print(f"  Original: {result_original} {'✓' if result_original == expected else '✗'}")
        print(f"  Solutions Match: {'✓' if result_optimized == result_original else '✗'}")
        print()


def analyze_space_complexity():
    """Demonstrate space complexity difference"""
    import sys
    
    print("Space Complexity Analysis:")
    print("=" * 50)
    print("Original Solution:")
    print("  - Uses dp array of size n")
    print("  - Space Complexity: O(n)")
    print("  - Memory usage grows linearly with input size")
    print()
    print("Space-Optimized Solution:")
    print("  - Uses only 2 variables (prev1, prev2)")
    print("  - Space Complexity: O(1)")
    print("  - Constant memory usage regardless of input size")
    print()
    
    # Example with large input
    n = 1000
    print(f"For n={n} steps:")
    print(f"  Original: ~{n * sys.getsizeof(0)} bytes for DP array")
    print(f"  Optimized: ~{2 * sys.getsizeof(0)} bytes for 2 variables")
    print(f"  Space savings: ~{((n-2)/n)*100:.1f}%")


if __name__ == "__main__":
    test_frog_jump_solutions()
    analyze_space_complexity()

# Example usage:
# heights = [10, 30, 40, 20]
# print(frog_jump_min_energy(heights))  # Output: 30