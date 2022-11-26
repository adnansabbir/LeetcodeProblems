class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        # sort each list according to the start time
        s = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        startTime = [x[0] for x in s]
        endTime   = [x[1] for x in s]
        profit    = [x[2] for x in s]

        # Bottom up dynammic programming 
        # Knapsack problem
        dp = [0] * n
        dp[-1] = profit[-1]
        for i in range(n-2, -1, -1):
            # If we include the current job
            # Add the current job to the maximum profit of the jobs that start when this job ends (if exists)
            j = bisect.bisect_left(startTime, endTime[i])
            # Decision to include job
            dp[i] = max(profit[i] + dp[j] if j < n else profit[i], dp[i+1])

        return dp[0]