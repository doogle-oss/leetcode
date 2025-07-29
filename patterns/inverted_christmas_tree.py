"""
Christmas Tree Pattern

Given a value n, print a Christmas tree of height n.
A Christmas tree starts narrow at the top and gets wider towards the bottom.

Example:
For n = 5:
    *
   ***
  *****
 *******
*********

Time Complexity: O(n²) - optimal for this problem as we need to print O(n²) characters
Space Complexity: O(1) - only using constant extra space
"""


def print_christmas_tree(n: int):
    """
    Print a Christmas tree of height n - Optimized solution

    Args:
        n (int): Height of the Christmas tree
    """
    if n <= 0:
        print("Height must be a positive integer")
        return

    # Optimized: Direct string construction with minimal operations
    for i in range(n):
        # Direct print with calculated spaces and stars
        # Row i: (n-i-1) spaces + (2*i+1) stars
        print(str(" " * (n - i - 1) + "*" * (2 * i + 1)))


def print_inverse_christmas_tree(n: int) -> None:
    """Print an inverted Christmas tree of height n

    Args:
        n (int): Height of the Christmas tree
    """
    if n <= 0:
        print("Height must be a positive integer")
        return

    for i in range(n):
        print(" " * i + "*" * (2 * (n - i - 1) + 1))


def print_horizontal_christmas_tree(n: int) -> None:
    """Print a horizontal Christmas tree of width n - Optimized solution

    A horizontal Christmas tree grows from left to right
    Example for n=5:
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *

    Time Complexity: O(n²) - optimal for this problem as we need to print O(n²) characters
    Space Complexity: O(1) - only using constant extra space

    Args:
        n (int): Width of the Christmas tree
    """
    if n <= 0:
        print("Width must be a positive integer")
        return

    # Optimized: Single loop with conditional logic
    for i in range(1, 2 * n):
        # For first half: print i stars (1 to n)
        # For second half: print (2*n - i) stars (n-1 to 1)
        stars = i if i <= n else 2 * n - i
        print("*" * stars)


def main():
    """
    Main function to demonstrate the Christmas tree pattern
    """
    print("Christmas Tree Pattern")
    print("=" * 40)

    # Get input from user
    try:
        n = 7

        print(f"\nChristmas Tree of height {n}:")
        print_christmas_tree(n)

    except ValueError:
        print("Please enter a valid integer")


# Test cases
def test_christmas_tree():
    """
    Test function with various inputs
    """
    print("\nTest Cases:")
    print("-" * 20)

    test_cases = [1, 3, 5, 7]

    for height in test_cases:
        print(f"\nHeight {height}:")
        print_christmas_tree(height)


if __name__ == "__main__":
    # main()
    # test_christmas_tree()
    print_inverse_christmas_tree(10)
    print_horizontal_christmas_tree(7)
