import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [sys.maxsize] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for dIdx in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dp[i] = min(dp[i], 1 + dp[dIdx])
        
        return dp[0]
        
