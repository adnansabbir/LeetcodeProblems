from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(maxsize=None)
        def climb(stair):
            if stair >= len(cost):
                return 0
            
            return cost[stair] + min(climb(stair + 1), climb(stair + 2))
        
        return min(climb(0), climb(1))
        