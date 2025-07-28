from typing import List

def rotting_eggs_days(grid: List[List[int]]) -> int:
    """
    Returns the number of days required to rot all eggs in the grid.
    -1: rotten egg, 0: good egg
    If not all eggs can rot, returns -1.
    Uses DFS to propagate rotting.
    """
    if not grid or not grid[0]:
        return -1
    m, n = len(grid), len(grid[0])
    from collections import deque
    days = [[-1 for _ in range(n)] for _ in range(m)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque()

    # Enqueue all rotten eggs as starting points
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                days[i][j] = 0
                queue.append((i, j, 0))

    # BFS propagation
    while queue:
        x, y, day = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                if days[nx][ny] == -1 or days[nx][ny] > day + 1:
                    days[nx][ny] = day + 1
                    queue.append((nx, ny, day + 1))

    max_day = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                if days[i][j] == -1:
                    return -1  # Not all eggs can rot
                max_day = max(max_day, days[i][j])
    return max_day


def test_rotting_eggs_days() -> None:
    grid1 = [
        [0, -1, 0],
        [0, 0, 0],
        [0, 0, -1]
    ]
    print(rotting_eggs_days(grid1))  # Output: 2

    grid2 = [
        [0, 0, 0],
        [0, -1, 0],
        [0, 0, 0]
    ]
    print(rotting_eggs_days(grid2))  # Output: 2

    grid3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(rotting_eggs_days(grid3))  # Output: -1 (no rotten egg)

    grid4 = [
        [-1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(rotting_eggs_days(grid4))  # Output: 4

    grid5 = [
        [0, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ]
    print(rotting_eggs_days(grid5))  # Output: -1 (egg can't rot)

if __name__ == "__main__":
    test_rotting_eggs_days()
