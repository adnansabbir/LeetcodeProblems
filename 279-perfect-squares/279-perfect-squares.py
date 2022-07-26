class Solution:
#     def numSquares(self, n: int) -> int:        
#         dp = [n] * (n+1)
#         dp[0] = 0
        
#         for i in range(1, n+1):
#             for j in range(1, int(sqrt(n)) + 1):
#                 val = j * j
#                 if i - val >= 0:
#                     dp[i] = min(dp[i], 1+dp[i-val])
#         return dp[-1]
    
    def numSquares(self, n: int) -> int:        
        dp = [n] * (n+1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, int(sqrt(n)) + 1):
                val = j * j
                if i - val >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-val])
        return dp[-1]
                