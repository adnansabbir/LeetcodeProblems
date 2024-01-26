from functools import lru_cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(maxsize=None)
        def countPath(i: int, j: int, movesLeft: int) -> int:
            if not (0 <= i < m and 0 <= j < n):
                return 1
            
            if not movesLeft:
                return 0
            
            return countPath(i+1, j, movesLeft - 1) + countPath(i-1, j, movesLeft - 1) + countPath(i, j + 1, movesLeft - 1) + countPath(i, j - 1, movesLeft - 1)
        
        return countPath(startRow, startColumn, maxMove) % (pow(10,9) + 7)
            

