from typing import List


def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence in the array.

    Time Complexity: O(n)
        - Uses a set for O(1) average time complexity for lookups.

    Space Complexity: O(n)
        - Stores the elements in a set.

    Parameters:
    nums (List[int]): The input array of integers.

    Returns:
    int: The length of the longest consecutive sequence.
    """
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# Example usage
if __name__ == "__main__":
    input_array = [100, 4, 200, 1, 3, 2]
    print(
        "Length of the longest consecutive sequence:",
        longest_consecutive_sequence(input_array),
    )
