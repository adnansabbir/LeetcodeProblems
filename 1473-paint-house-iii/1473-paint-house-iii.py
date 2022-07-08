import sys
from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @lru_cache(maxsize = None)
        def findMinCost(currentIndex, prevColor, neighbourhoodCount):
            if neighbourhoodCount > target:
                return sys.maxsize
            
            if currentIndex == len(houses):
                return 0 if neighbourhoodCount == target else sys.maxsize
            
            minCost = sys.maxsize
            
            if houses[currentIndex] != 0:
                neighbourhoodCount += (1 if houses[currentIndex] != prevColor else 0)
                minCost = findMinCost(currentIndex+1, houses[currentIndex], neighbourhoodCount)
            else:
                for color in range(1, n+1):
                    nc = neighbourhoodCount + (0 if color == prevColor else 1)
                    currentCost = cost[currentIndex][color-1] + findMinCost(currentIndex+1, color, nc)
                    
                    minCost = min(minCost, currentCost)
            
            return minCost
        
        result = findMinCost(0,0,0)
        return result if result != sys.maxsize else -1
            
            
            
            
        