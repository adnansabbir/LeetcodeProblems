class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid) * len(grid[0])
        
        def getMatrixPos(idx: int)-> list[int]:
            return [idx//len(grid[0]), idx % len(grid[0])]
        
        k = k%n
        if not k:
            return grid
        
        start = 0
        curr = start
        tempVal = grid[0][0]
        
        for i in range(n):
            curr = (curr + k) % n
            cx, cy = getMatrixPos(curr)
            grid[cx][cy], tempVal = tempVal, grid[cx][cy]
            
            if curr == start:
                start +=1
                curr = start
                x,y = getMatrixPos(curr)
                tempVal = grid[x][y]
        
        return grid
            
            