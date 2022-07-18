from functools import lru_cache

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                # if i == 3:
                    # print(i, j, j-i+1, j+1, dp[i-1][max(j-i+1, 0):j+1])
                dp[i][j] = sum(dp[i-1][ max(j-i+1, 0) : j+1]) % 1000000007
            # print(dp)
        
        return dp[-1][-1]
                