class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def isEqual(r: int, j: int)-> bool:
            for i in range(n):
                if grid[r][i] != grid[i][j]:
                    return False
            return True
        
        result = 0
        for r in range(n):
            for c in range(n):
                if isEqual(r, c):
                    result +=1
        
        return result