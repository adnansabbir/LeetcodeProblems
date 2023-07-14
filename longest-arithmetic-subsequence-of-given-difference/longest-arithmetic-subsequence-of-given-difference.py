class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [1]*n
        numIndex = {}
        result = 1
        for i in range(n - 1, -1, -1):
            print(i)
            target = arr[i] + difference
            if target in numIndex:
                dp[i] += dp[numIndex[target]]
            
            result = max(result, dp[i])
            numIndex[arr[i]] = i
        
        return result