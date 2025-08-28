class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # sort bottom triangle
        def getDiagonalVals(x, y):
            result = []
            while x < m and y < n:
                result.append(grid[x][y])
                x += 1
                y += 1
            return result
        
        def setDiagonalVals(x, y, vals):
            while vals:
                grid[x][y] = vals.pop(0)
                x += 1
                y += 1

        for row in range(m):
            vals = getDiagonalVals(row, 0)
            vals.sort(reverse=True)
            setDiagonalVals(row, 0, vals)
        
        for col in range(1, n):
            vals = getDiagonalVals(0, col)
            vals.sort()
            setDiagonalVals(0, col, vals)

        return grid
        