from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        sortedEvents = sorted(events, key = lambda x: (x[0], x[1], -x[2]))
        # print(sortedEvents)

        def getNextEventIndex(fromIdx: int, busyTill: int)-> int:
            start, end = fromIdx + 1, n - 1
            while start <= end:
                mid = (start + end) // 2
                if sortedEvents[mid][0] > busyTill and sortedEvents[mid - 1][0] <= busyTill:
                    return mid
                elif sortedEvents[mid][0] <= busyTill:
                    start = mid + 1
                else:
                    end = mid - 1
            return n
        
        @lru_cache(maxsize = None)
        def dp(currIdx: int, remainingEvents: int)-> int:
            if currIdx >= n or not remainingEvents:
                return 0
            
            [start, end, value] = sortedEvents[currIdx]
            withCurrent = 0
            withOutCurrent = 0
            
            withOutCurrent = dp(currIdx + 1, remainingEvents)
            nextEventIdx = getNextEventIndex(currIdx, end)
            # print(currIdx, nextEventIdx)
            withCurrent =  value + dp(nextEventIdx, remainingEvents - 1)
            
            # print(currIdx, [start, end, value], withCurrent, withOutCurrent,  max(withCurrent, withOutCurrent))
            return max(withCurrent, withOutCurrent)
            

        return dp(0, k)