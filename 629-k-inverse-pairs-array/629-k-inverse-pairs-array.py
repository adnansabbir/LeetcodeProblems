from functools import lru_cache

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]
        M = 1000000007
        for i in range(1,n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                value = (dp[i-1][j] + M - (dp[i-1][j-i] if (j-i)>=0 else 0)) % M
                dp[i][j] = (value + dp[i][j-1]) % M
        
        return (dp[n][k] + M - (dp[n][k-1] if k > 0 else 0)) % M
                