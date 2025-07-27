def get_divisors(n):
    """
    Returns all divisors of n in O(sqrt(n)) time and O(1) extra space (excluding output).
    """
    if n < 1:
        return []
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)


def test_get_divisors():
    print(get_divisors(1))    # [1]
    print(get_divisors(12))   # [1, 2, 3, 4, 6, 12]
    print(get_divisors(25))   # [1, 5, 25]
    print(get_divisors(36))   # [1, 2, 3, 4, 6, 9, 12, 18, 36]
    print(get_divisors(49))   # [1, 7, 49]

if __name__ == "__main__":
    test_get_divisors()
