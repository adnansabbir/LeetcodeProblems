class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        result = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]

            result += 1 if abs(left - right) % 2 == 0 else 0
        
        return result
        