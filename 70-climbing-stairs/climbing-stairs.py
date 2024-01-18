class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [1,2]

        for i in range(3, n + 1):
            dp.append(dp[0] + dp[1])
            dp.pop(0)
        
        return dp[-1]