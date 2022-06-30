class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        reverseSum = [nums[-1]]
            
        for num in reversed(nums[:-1]):
            reverseSum.append(reverseSum[-1] + num)
        
        leftSum = 0
        for i in range(0, len(nums)):
            leftSum += nums[i]
            if leftSum == reverseSum[len(nums) - i - 1]:
                return i
        
        return -1
        