import math

class Solution:
    def timeToFinish(self, hour: int, piles: List[int], h: int)-> bool:
        return sum([(math.ceil(p/hour)) for p in piles])
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)+1
        
        min_time = end
        while start<=end:
            mid = (start+end)//2
            
            completeTime = self.timeToFinish(mid, piles, h)
            if completeTime <= h:
                min_time = min(min_time, mid)
                end = mid-1
            else:
                start = mid+1
        
        return min_time
