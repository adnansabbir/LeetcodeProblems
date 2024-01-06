from functools import lru_cache

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        startEndProfit = sorted([(s,e,p) for s,e,p in zip(startTime, endTime, profit)], key = lambda x: x[0])
        n = len(startTime)

        def getNextIndexWithGreaterStartTime(time: int, start: int, end: int)-> int:
            while start <= end:
                mid = (start + end) // 2

                if startEndProfit[mid][0] >= time and (mid == start or startEndProfit[mid-1][0] < time):
                    return mid
                elif startEndProfit[mid][0] >= time:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return -1

        @lru_cache(maxsize = None)
        def countMaxProfit(currIndex: int)-> int:
            if currIndex == n:
                return 0
            
            nextJobIdx = getNextIndexWithGreaterStartTime(startEndProfit[currIndex][1], currIndex + 1, n - 1)
            nextJobIdx = n if nextJobIdx == -1 else nextJobIdx

            result = max(
                startEndProfit[currIndex][2] + countMaxProfit(nextJobIdx),
                countMaxProfit(currIndex + 1)
            )

            return result

        return countMaxProfit(0)