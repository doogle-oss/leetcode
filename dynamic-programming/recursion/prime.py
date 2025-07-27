def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    print(is_prime(1))   # False
    print(is_prime(2))   # True
    print(is_prime(3))   # True
    print(is_prime(4))   # False
    print(is_prime(17))  # True
    print(is_prime(18))  # False
    print(is_prime(97))  # True
    print(is_prime(100)) # False

if __name__ == "__main__":
    test_is_prime()
