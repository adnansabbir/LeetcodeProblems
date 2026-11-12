class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                inc = 1
            
            if nums[i] < nums[i - 1]:
                dec += 1
            else:
                dec = 1
            
            res = max(res, inc, dec)
        return res
        