class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['.' if (i == 0 or j == m - 1) else '#' for i in range(n)] for j in range(m)]
        grid = [''.join(g) for g in grid]
        return grid
        