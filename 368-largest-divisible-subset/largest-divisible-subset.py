class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n_len = len(nums)
        if n_len < 2:
            return nums
        
        nums.sort()
        
        dp = [(0, 0)] * n_len
        dp[0] = (1, 0)
        
        maxIndex, maxVal = 0, (1,1)
        
        for i in range(1, n_len):
            dp[i] = max((dp[j][0] + 1, j) for j in range(i + 1) if nums[i] % nums[j] is 0)
            if dp[i] > maxVal:
                maxIndex, maxVal = i, dp[i]
        
        i, lds = maxIndex, [nums[maxIndex]]
        
        while i != dp[i][1]:
            i = dp[i][1]
            lds.append(nums[i])
        return lds