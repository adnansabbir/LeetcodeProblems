from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if (startRow == m or startRow < 0) or (startColumn == n or startColumn < 0):
            return 1
        if maxMove == 0:
            return 0
        
        return (
            self.findPaths(m,n,maxMove-1, startRow-1, startColumn) 
            + self.findPaths(m,n,maxMove-1, startRow+1, startColumn) 
            + self.findPaths(m,n,maxMove-1, startRow, startColumn-1) 
            + self.findPaths(m,n,maxMove-1, startRow, startColumn+1)
        ) % (pow(10,9) + 7)
        