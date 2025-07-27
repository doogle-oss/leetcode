def gcd(a, b):
    """
    Returns the greatest common divisor (GCD) of a and b using Euclidean algorithm.
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1) (iterative)
    """
    while b:
        a, b = b, a % b
    return abs(a)


def hcf(a, b):
    """
    Returns the highest common factor (HCF) of a and b.
    HCF is the same as GCD.
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1)
    """
    return gcd(a, b)


def test_gcd():
    print(gcd(12, 18))   # 6
    print(gcd(100, 25))  # 25
    print(gcd(7, 13))    # 1
    print(gcd(36, 60))   # 12
    print(gcd(0, 5))     # 5
    print(gcd(0, 0))     # 0


def test_hcf():
    print(hcf(12, 18))   # 6
    print(hcf(100, 25))  # 25
    print(hcf(7, 13))    # 1
    print(hcf(36, 60))   # 12
    print(hcf(0, 5))     # 5
    print(hcf(0, 0))     # 0


if __name__ == "__main__":
    test_gcd()
    test_hcf()
