class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def explore(x,y)-> int:
            if (0 > x or x >= len(grid)) or (0 > y or y >= len(grid[0])) or not grid[x][y]:
                return 0
            
            grid[x][y] = 0
            return 1 + explore(x-1, y) + explore(x+1, y) + explore(x, y-1) + explore(x, y+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_area = max(max_area, explore(i,j))
        
        return max_area
        