def sum_n(n):
    """
    Returns the sum of numbers from 1 to n using recursion.
    """
    if n <= 0:
        return 0
    return n + sum_n(n-1)


def sum_n_functional(n):
    """
    Functional recursion: returns sum of 1 to n.
    """
    if n <= 0:
        return 0
    return n + sum_n_functional(n-1)


def sum_n_parametrized(n, acc=0):
    """
    Parametrized recursion: accumulates sum in acc.
    Prints the result for demonstration.
    """
    if n < 1:
        print(acc)
        return acc
    return sum_n_parametrized(n-1, acc+n)


def factorial_functional(n):
    """
    Functional recursion: returns factorial of n.
    """
    if n <= 1:
        return 1
    return n * factorial_functional(n-1)


def test_sum_n():
    print(sum_n(0))   # 0
    print(sum_n(1))   # 1
    print(sum_n(5))   # 15
    print(sum_n(10))  # 55
    print(sum_n(100)) # 5050


def test_sum_n_methods():
    print("Functional recursion:")
    print(sum_n_functional(5))   # 15
    print(sum_n_functional(10))  # 55
    print("\nParametrized recursion:")
    sum_n_parametrized(5)        # 15
    sum_n_parametrized(10)       # 55


def test_factorial_functional():
    print(factorial_functional(0))   # 1
    print(factorial_functional(1))   # 1
    print(factorial_functional(5))   # 120
    print(factorial_functional(10))  # 3628800


if __name__ == "__main__":
    test_sum_n()
    test_sum_n_methods()
    test_factorial_functional()
