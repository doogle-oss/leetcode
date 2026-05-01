from collections import deque
from pprint import pp
from typing import MutableSequence, Any

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def append_rottens(rotten, grid, rr, rc, minutes, rows, cols, fresh):
  for dr, dc in directions:
    nr, nc = rr + dr, rc + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
      grid[nr][nc] = 2
      fresh -= 1
      rotten.append(((nr, nc), minutes + 1))
  return fresh


def oranges_rotting_bfs(grid: MutableSequence[MutableSequence[int]]) -> int:
  if not grid or not grid[0]:
    return 0

  cols, fresh, rows, rotten = get_fresh_rotten_oranges(grid)
  if fresh == 0:
    return 0
  minutes = 0
  while rotten:
    (rr, rc), minutes = rotten.popleft()
    fresh = append_rottens(rotten, grid, rr, rc, minutes, rows, cols, fresh)
  return minutes if fresh == 0 else -1


def get_fresh_rotten_oranges(grid: MutableSequence[MutableSequence[int]]) -> \
    tuple[int, int, int, deque[Any]]:
  rows = len(grid)
  cols = len(grid[0])

  fresh, rotten = process_orange_grid(grid)
  return cols, fresh, rows, rotten


def process_orange_grid(grid: MutableSequence[MutableSequence[int]]) -> tuple[
  int, deque[Any]]:
  fresh = 0
  stack = deque()
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == 1:
        fresh += 1
      elif grid[r][c] == 2:
        stack.append(((r, c), 0))
  return fresh, stack


def _run_examples() -> None:
  examples = [([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4,),
              ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1,), ([[0, 2]], 0,),
              ([[1]], -1,), ([[]], 0,), ]

  for i, (grid, expected) in enumerate(examples, start=1):
    _run_example(grid, expected, i)


def _run_example(grid: MutableSequence[MutableSequence[int]], expected: int,
    i: int) -> None:
  grid_copy = [row[:] for row in grid]
  result = oranges_rotting_bfs(grid_copy)
  for r in grid:
    pp(r)
  print(f"Example {i}: {result} (expected {expected})")
  assert result == expected


if __name__ == "__main__":
  _run_examples()
