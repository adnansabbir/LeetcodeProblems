from functools import lru_cache
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the start time, end time, and profit into one list and sort it
        startEndProfit = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)], key=lambda x: x[0])
        n = len(startTime)

        # Binary search helper function to find the next job index with a start time greater than the given time
        def getNextIndexWithGreaterStartTime(time: int, start: int, end: int) -> int:
            while start <= end:
                mid = (start + end) // 2

                if startEndProfit[mid][0] >= time and (mid == start or startEndProfit[mid-1][0] < time):
                    return mid
                elif startEndProfit[mid][0] >= time:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return -1

        # Recursive function to count the max profit using memoization
        @lru_cache(maxsize=None)
        def countMaxProfit(currIndex: int) -> int:
            if currIndex == n:
                return 0
            
            # Find the next job index that starts after the current job ends
            nextJobIdx = getNextIndexWithGreaterStartTime(startEndProfit[currIndex][1], currIndex + 1, n - 1)
            nextJobIdx = n if nextJobIdx == -1 else nextJobIdx

            # Calculate the max profit by either taking the current job and adding the profit from the next available job or skipping the current job
            result = max(
                startEndProfit[currIndex][2] + countMaxProfit(nextJobIdx),
                countMaxProfit(currIndex + 1)
            )

            return result

        return countMaxProfit(0)
