import math
import sys
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        totalDistance = sum(dist)
        if hour <= n - 1:
            return -1
        if totalDistance <= hour:
            return 1
        
        def canComplete(speed: int)-> bool:
            if speed == 0:
                return False
            totalTime = 0
            for i, distance in enumerate(dist):
                if i == n-1:
                    totalTime += distance/speed
                else:
                    totalTime += math.ceil(distance/speed)
            
            return totalTime <= hour
        
        start, end = 1, 10000000
        while start <= end:
            mid = (start + end) // 2
            if canComplete(mid) and (mid == 0 or not canComplete(mid - 1)):
                return mid
            elif canComplete(mid):
                end = mid - 1
            else:
                start = mid + 1

        return -1

        