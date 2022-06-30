class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in reversed(range(len(nums)-1)):
            nums[i] += nums[i+1]
        
        leftSum = 0
        for i in range(0, len(nums)):
            leftSum += nums[i] - (nums[i+1] if i+1 != len(nums) else 0)
            if leftSum == nums[i]:
                return i
        
        return -1
        