def ninja_training(points):
    """
    points: List[List[int]]
    points[day][task] = points for doing task (0,1,2) on day
    Ninja can't do the same task on consecutive days.
    Returns the maximum points possible.
    """
    if not points:
        return 0
    n = len(points)
    # dp[day][last_task]: max points up to 'day' if last_task was done yesterday
    dp = [[0]*4 for _ in range(n)]
    # Base case: first day, last_task = 3 (no task done previously)
    for last in range(4):
        dp[0][last] = max(points[0][task] for task in range(3) if task != last)
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    val = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last], val)
    return dp[n-1][3]


def ninja_training_space_optimized(points):
    """
    Space-optimized DP for ninja training problem.
    Only keeps track of previous day's results.
    """
    if not points:
        return 0
    n = len(points)
    prev = [0, 0, 0, 0]  # prev[last_task]: max points up to previous day
    # Base case: first day
    for last in range(4):
        prev[last] = max(points[0][task] for task in range(3) if task != last)
    for day in range(1, n):
        curr = [0, 0, 0, 0]
        for last in range(4):
            curr[last] = 0
            for task in range(3):
                if task != last:
                    val = points[day][task] + prev[task]
                    curr[last] = max(curr[last], val)
        prev = curr
    return prev[3]


def test_ninja_training():
    points1 = [
        [10, 40, 70],
        [20, 50, 80],
        [30, 60, 90]
    ]
    # Optimal: 70 (day0, task2) + 50 (day1, task1) + 90 (day2, task2) = 210
    print("Test 1:", ninja_training(points1))  # Output: 210

    points2 = [
        [1, 2, 5],
        [3, 1, 1],
        [3, 3, 3]
    ]
    print("Test 2:", ninja_training(points2))  # Output: 11


def test_ninja_training_space_optimized():
    points1 = [
        [10, 40, 70],
        [20, 50, 80],
        [30, 60, 90]
    ]
    print("Space Optimized Test 1:", ninja_training_space_optimized(points1))  # Output: 210

    points2 = [
        [1, 2, 5],
        [3, 1, 1],
        [3, 3, 3]
    ]
    print("Space Optimized Test 2:", ninja_training_space_optimized(points2))  # Output: 11


if __name__ == "__main__":
    test_ninja_training()
    test_ninja_training_space_optimized()

# Example usage:
# points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
# print(ninja_training_space_optimized(points))  # Output: 210
