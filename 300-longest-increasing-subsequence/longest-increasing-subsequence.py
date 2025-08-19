class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        def sub_seq_len(idx)-> int:
            if idx == len(nums):
                return 0
            
            if dp[idx] != 0:
                return dp[idx]
            
            dp[idx] = 1
            for next_idx in range(idx+1, len(nums)):
                if nums[next_idx] > nums[idx]:
                    dp[idx] = max(dp[idx], 1 + sub_seq_len(next_idx))
            return dp[idx]

        for i in range(len(nums)):
            dp[i] = sub_seq_len(i)
        
        return max(dp)



        