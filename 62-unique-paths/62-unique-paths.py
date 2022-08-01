class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        
        def getVal(i: int, j: int)-> int:
            if i < 0 or j < 0:
                return 0
            return dp[i][j]
        
        for i in range(m):
            for j in range(n):
                if(i+j == 0):
                    continue
                dp[i][j] = getVal(i-1, j) + getVal(i, j-1)
        
        return dp[-1][-1]
        