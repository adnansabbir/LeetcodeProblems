class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums) - nums[0]
        left = nums[0]

        result = 1 if left >= right else 0

        for i in range(1, len(nums) - 1):
            right -= nums[i]
            left += nums[i]

            if left >= right:
                result += 1

        return result
        