class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        x1,y1,x2,y2 = m, n, 0, 0 

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    x1 = min(x1, row)
                    x2 = max(x2, row)
                    y1 = min(y1, col)
                    y2 = max(y2, col)
        
        height = x2 - x1 + 1
        width = y2 - y1 + 1

        return height * width

        