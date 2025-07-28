def sum_n(n: int) -> int:
    """
    Returns the sum of numbers from 1 to n using recursion.
    """
    if n <= 0:
        return 0
    return n + sum_n(n-1)


def sum_n_functional(n: int) -> int:
    """
    Functional recursion: returns sum of 1 to n.
    """
    if n <= 0:
        return 0
    return n + sum_n_functional(n-1)


def sum_n_parametrized(n: int, acc: int = 0) -> int:
    """
    Parametrized recursion: accumulates sum in acc.
    Prints the result for demonstration.
    """
    if n < 1:
        print(acc)
        return acc
    return sum_n_parametrized(n-1, acc+n)


def factorial_functional(n: int) -> int:
    """
    Functional recursion: returns factorial of n.
    """
    if n <= 1:
        return 1
    return n * factorial_functional(n-1)


def reverse_array_rec(arr: list, start: int = 0, end: int = None) -> None:
    """
    Reverses the array in place using recursion.
    """
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array_rec(arr, start+1, end-1)


def is_palindrome_rec(s: str, start: int = 0, end: int = None) -> bool:
    """
    Checks if a string is a palindrome using recursion.
    Returns True if palindrome, False otherwise.
    """
    if end is None:
        end = len(s) - 1
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome_rec(s, start+1, end-1)


def fibonacci_rec(n: int) -> int:
    """
    Returns the nth Fibonacci number using recursion.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_memo(n: int, memo: dict = None) -> int:
    """
    Returns the nth Fibonacci number using recursion with memoization.
    Time: O(n), Space: O(n)
    """
    if memo is None:
        memo = {}
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]


def fibonacci_space_optimized(n: int) -> int:
    """
    Returns the nth Fibonacci number using space-optimized iteration.
    Time: O(n), Space: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    prev2, prev1 = 0, 1
    for _ in range(2, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1


def test_sum_n() -> None:
    print(sum_n(0))   # 0
    print(sum_n(1))   # 1
    print(sum_n(5))   # 15
    print(sum_n(10))  # 55
    print(sum_n(100)) # 5050


def test_sum_n_methods() -> None:
    print("Functional recursion:")
    print(sum_n_functional(5))   # 15
    print(sum_n_functional(10))  # 55
    print("\nParametrized recursion:")
    sum_n_parametrized(5)        # 15
    sum_n_parametrized(10)       # 55


def test_factorial_functional() -> None:
    print(factorial_functional(0))   # 1
    print(factorial_functional(1))   # 1
    print(factorial_functional(5))   # 120
    print(factorial_functional(10))  # 3628800


def test_reverse_array_rec() -> None:
    arr1 = [1, 2, 3, 4, 5]
    reverse_array_rec(arr1)
    print(arr1)  # [5, 4, 3, 2, 1]
    arr2 = [10, 20, 30]
    reverse_array_rec(arr2)
    print(arr2)  # [30, 20, 10]
    arr3 = []
    reverse_array_rec(arr3)
    print(arr3)  # []


def test_is_palindrome_rec() -> None:
    print(is_palindrome_rec("racecar"))   # True
    print(is_palindrome_rec("madam"))     # True
    print(is_palindrome_rec("hello"))     # False
    print(is_palindrome_rec("a"))         # True
    print(is_palindrome_rec(""))          # True
    print(is_palindrome_rec("abccba"))    # True
    print(is_palindrome_rec("abcba"))     # True
    print(is_palindrome_rec("abca"))      # False


def test_fibonacci_rec() -> None:
    print(fibonacci_rec(0))   # 0
    print(fibonacci_rec(1))   # 1
    print(fibonacci_rec(5))   # 5
    print(fibonacci_rec(10))  # 55
    print(fibonacci_rec(15))  # 610


def test_fibonacci_optimized() -> None:
    print("Memoized Fibonacci:")
    print(fibonacci_memo(0))   # 0
    print(fibonacci_memo(1))   # 1
    print(fibonacci_memo(10))  # 55
    print(fibonacci_memo(20))  # 6765
    print(fibonacci_memo(30))  # 832040
    print("Space Optimized Fibonacci:")
    print(fibonacci_space_optimized(0))   # 0
    print(fibonacci_space_optimized(1))   # 1
    print(fibonacci_space_optimized(10))  # 55
    print(fibonacci_space_optimized(20))  # 6765
    print(fibonacci_space_optimized(30))  # 832040


if __name__ == "__main__":
    test_sum_n()
    test_sum_n_methods()
    test_factorial_functional()
    test_reverse_array_rec()
    test_is_palindrome_rec()
    test_fibonacci_rec()
    test_fibonacci_optimized()
