from functools import cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        
        cm = {0:[1], 1:[0,2], 2:[0,1,3,4], 3:[2,4], 4:[0]}
        maxNum = pow(10,9) + 7
        cidx = 1
        prevIdx = 0
        
        dp = [[1,1,1,1,1],[0,0,0,0,0]]
        
        for _ in range(1,n):
            for i in range(5):
                dp[cidx][i] = sum(dp[prevIdx][j] for j in cm[i]) % maxNum
            
            cidx, prevIdx = prevIdx, cidx
        
        return sum(dp[prevIdx]) % maxNum