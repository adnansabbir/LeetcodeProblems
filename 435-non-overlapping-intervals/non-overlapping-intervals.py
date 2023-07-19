class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        intervals.sort()
        starts = [start for [start, end] in intervals]
        dp = [1] * (n + 1)
        
        def getNextEvent(endTime: int)-> int:
            i = bisect.bisect_left(starts, endTime)
            if i == n:
                return None
            return i

        # print(intervals)
        for i in range(n-1, -1, -1):
            [start, end] = intervals[i]
            j = getNextEvent(end)
            if j == None:
                dp[i] = max(dp[i], dp[i+1])
            else:
                dp[i] = max(dp[i], dp[j] + 1, dp[i+1])

        # print(dp)
        return n - dp[0]