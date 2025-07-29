from typing import List


def alternate_positive_negative(arr: List[int]) -> List[int]:
    """
    Rearranges the array to alternate between positive and negative numbers.

    Time Complexity: O(n)
        - Separating positive and negative numbers takes O(n).
        - Alternating and appending remaining elements also takes O(n).

    Space Complexity: O(n)
        - Additional space is used for the positive and negative lists.

    Parameters:
    arr (List[int]): The input array containing integers.

    Returns:
    List[int]: A new array with alternating positive and negative numbers.
    """
    # Separate positive and negative numbers
    positive: List[int] = [num for num in arr if num >= 0]
    negative: List[int] = [num for num in arr if num < 0]

    result: List[int] = []
    i, j = 0, 0

    # Alternate between positive and negative numbers
    while i < len(positive) and j < len(negative):
        result.append(positive[i])
        result.append(negative[j])
        i += 1
        j += 1

    # Append remaining positive or negative numbers
    result.extend(positive[i:])
    result.extend(negative[j:])

    return result


def alternate_positive_negative_inplace(arr: List[int]) -> None:
    """
    Rearranges the array to alternate between positive and negative numbers in-place.

    Time Complexity: O(n)
        - Rearranging elements takes O(n).

    Space Complexity: O(1)
        - No additional space is used.

    Parameters:
    arr (List[int]): The input array containing integers. The array is modified in-place.

    Returns:
    None
    """

    def swap(i: int, j: int) -> None:
        """Helper function to swap two elements in the array."""
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    pos, neg = 0, 1  # Pointers for positive and negative indices

    print("Iteration | pos | neg | Array")
    print("--------------------------------")

    iteration = 0
    while pos < n and neg < n:
        # Print the current state before processing
        print(f"{iteration:9} | {pos:3} | {neg:3} | {arr}")

        # Find the next misplaced positive number
        while pos < n and arr[pos] >= 0:
            pos += 2

        # Find the next misplaced negative number
        while neg < n and arr[neg] < 0:
            neg += 2

        # Swap misplaced elements
        if pos < n and neg < n:
            swap(pos, neg)

        iteration += 1

    # Print the final state
    print(f"{iteration:9} | {pos:3} | {neg:3} | {arr}")


# Example usage
if __name__ == "__main__":
    input_array: List[int] = [1, 2, -3, -4, 5, -6, -7, 8, -1, -3, -10]
    print(alternate_positive_negative(input_array))

    input_array_inplace: List[int] = [1, 2, -3, -4, 5, -6, -7, 8, -1, -3, -10, -98, -4]
    alternate_positive_negative_inplace(input_array_inplace)
    print("Final Array:", input_array_inplace)
