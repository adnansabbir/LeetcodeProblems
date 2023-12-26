from functools import lru_cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(maxsize=None)
        def numberOfWaysToTarget(n: int, diffFromTarget: int) -> int:
            if n == 0 and diffFromTarget == 0:
                return 1
            
            if diffFromTarget < 0 or n < 1:
                return 0
            
            numberOfWays = 0
            for face in range(1, k + 1):
                numberOfWays += numberOfWaysToTarget(n-1, diffFromTarget - face)
            
            return numberOfWays % ((10**9) + 7)
        
        return numberOfWaysToTarget(n, target)