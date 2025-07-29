from typing import List


def find_leaders(arr: List[int]) -> List[int]:
    """
    Finds all leaders in the array. A leader is an element that is greater than all the elements to its right.

    Time Complexity: O(n)
        - Traverses the array once from right to left.

    Space Complexity: O(n)
        - Stores the leaders in a list.

    Parameters:
    arr (List[int]): The input array of integers.

    Returns:
    List[int]: A list of leaders in the array.
    """
    n = len(arr)
    if n == 0:
        return []

    leaders: List[int] = []
    max_from_right: int = arr[-1]
    leaders.append(max_from_right)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)

    # Reverse the list to maintain the order of leaders as in the array
    leaders.reverse()
    return leaders


# Example usage
if __name__ == "__main__":
    input_array: List[int] = [16, 17, 4, 3, 5, 2]
    print("Leaders in the array:", find_leaders(input_array))
