# dynamic-programming/fibonacci.py
def fibonacci_space_optimized(n):
    """
    Space-optimized dynamic programming
    Time Complexity: O(n)
    Space Complexity: O(1) - only use two variables
    """
    if n <= 1:
        return n
    
    prev2 = 0  # F(0)
    prev1 = 1  # F(1)
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

if __name__ == "__main__":
    n = 2  # Example input
    print(f"Fibonacci of {n}: {fibonacci_space_optimized(n)}")
