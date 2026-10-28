from ast import List
class Solution:

  def createGrid(self, m: int, n: int) -> List[str]:
    # Strategy: Make the entire first row free cells ('.'),
    # and for the rest of the rows, only the last column is free ('.').
    # All other cells are obstacles ('#').

    grid = []

    # First row: all free
    grid.append('.' * n)

    # Remaining rows: only the last column is free
    for _ in range(1, m):
      row = '#' * (n - 1) + '.'
      grid.append(row)

    return grid