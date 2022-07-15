class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def explore(x,y)-> int:
            area = 0
            stack = [[x,y]]
            grid[x][y] = 0
            while stack:
                size = len(stack)
                area += size
                for _ in range(size):
                    _x,_y = stack.pop()
                    if _x > 0 and grid[_x-1][_y]:
                        stack.append([_x-1, _y])
                        grid[_x-1][_y] = 0
                    
                    if _x+1 < len(grid) and grid[_x+1][_y]:
                        stack.append([_x+1, _y])
                        grid[_x+1][_y] = 0
                    
                    if _y > 0 and grid[_x][_y-1]:
                        stack.append([_x, _y-1])
                        grid[_x][_y-1] = 0
                        
                    if _y+1 < len(grid[0]) and grid[_x][_y+1]:
                        stack.append([_x, _y+1])
                        grid[_x][_y+1] = 0
            return area
                    
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_area = max(max_area, explore(i,j))
        
        return max_area
        