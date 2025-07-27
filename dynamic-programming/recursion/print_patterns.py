def print_name_n_times(name, n):
    """
    Prints the given name n times using recursion.
    """
    if n == 0:
        return
    print(name)
    print_name_n_times(name, n-1)


def print_1_to_n(n, current=1):
    """
    Prints numbers from 1 to n linearly using recursion.
    """
    if current > n:
        return
    print(current)
    print_1_to_n(n, current+1)


def print_n_to_1(n):
    """
    Prints numbers from n to 1 linearly using recursion.
    """
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)


def print_1_to_n_backtrack(n):
    """
    Prints numbers from 1 to n using backtracking recursion.
    """
    def helper(i):
        if i < 1:
            return
        helper(i-1)
        print(i)
    helper(n)


def print_n_to_1_backtrack(n):
    """
    Prints numbers from n to 1 using backtracking recursion.
    """
    def helper(i):
        if i < 1:
            return
        print(i)
        helper(i-1)
    helper(n)


def test_print_patterns():
    print("Print name 'Alice' 3 times:")
    print_name_n_times('Alice', 3)
    print("\nPrint 1 to 5 linearly:")
    print_1_to_n(5)
    print("\nPrint 5 to 1 linearly:")
    print_n_to_1(5)
    print("\nPrint 1 to 5 using backtracking:")
    print_1_to_n_backtrack(5)
    print("\nPrint 5 to 1 using backtracking:")
    print_n_to_1_backtrack(5)

if __name__ == "__main__":
    test_print_patterns()
