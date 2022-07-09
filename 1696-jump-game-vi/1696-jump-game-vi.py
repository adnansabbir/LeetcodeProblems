class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        dp[n-1] = nums[n-1]
        queue = [n-1]
        
        for i in range(len(nums)-2, -1, -1):
            dp[i] = nums[i] + dp[queue[0]]
            if queue[0] - i >= k:
                queue.pop(0)
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            
            queue.append(i)
        
        return dp[0]