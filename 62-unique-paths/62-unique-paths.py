class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [0]*n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                dp[j] += dp[j-1] if j > 0 else 0
        
        return dp[-1]
        