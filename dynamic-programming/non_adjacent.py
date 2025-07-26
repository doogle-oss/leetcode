def max_sum_non_adjacent_optimized(nums):
    """
    Space-optimized approach: O(n) time, O(1) space
    Returns the maximum sum of non-adjacent elements.
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    for i in range(2, n):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    return prev1


def test_max_sum_non_adjacent():
    test_cases = [
        ([3, 2, 5, 10, 7], 15),   # 3 + 10 + 2 = 15
        ([2, 1, 4, 9], 11),       # 2 + 9 = 11
        ([5, 5, 10, 100, 10, 5], 110), # 5+100+5=110
        ([1, 2, 3], 4),           # 1+3=4
        ([10], 10),               # single element
        ([], 0),                  # empty array
        ([4, 1, 1, 4, 2, 1], 9),  # 4+4+1=9
    ]
    print("Testing Maximum Sum of Non-Adjacent Elements:")
    print("=" * 50)
    for i, (nums, expected) in enumerate(test_cases, 1):
        result_opt = max_sum_non_adjacent_optimized(nums)
        print(f"Test {i}: nums={nums}")
        print(f"  Optimized:  {result_opt} {'✓' if result_opt == expected else '✗'}")


def max_sum_non_adjacent_circle(nums):
    """
    House Robber II (circular):
    Cannot take both first and last element. Use space-optimized approach.
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
     # Exclude first or last house
    return max(max_sum_non_adjacent_optimized(nums[1:]), max_sum_non_adjacent_optimized(nums[:-1]))


def test_max_sum_non_adjacent_circle():
    test_cases = [
        ([2, 3, 2], 3),           # Rob house 2
        ([1, 2, 3, 1], 4),        # Rob houses 2 and 4
        ([0], 0),                 # Only one house
        ([1, 2, 1, 1], 2),        # Rob house 2
        ([5, 1, 1, 5], 10),       # Rob houses 1 and 4
        ([4, 1, 2, 7, 5, 3, 1], 14), # Rob 1, 4, 6
    ]
    print("Testing Maximum Sum of Non-Adjacent Elements (Circle):")
    print("=" * 50)
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = max_sum_non_adjacent_circle(nums)
        print(f"Test {i}: nums={nums}")
        print(f"  Circle: {result} {'✓' if result == expected else '✗'}\n")


if __name__ == "__main__":
    test_max_sum_non_adjacent()
    test_max_sum_non_adjacent_circle()

# Example usage:
# nums = [2, 3, 2]
# print(max_sum_non_adjacent_circle(nums))  # Output: 3
