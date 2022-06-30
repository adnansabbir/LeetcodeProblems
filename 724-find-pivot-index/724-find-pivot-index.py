class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1 = [nums[0]]
        sum2 = [nums[-1]]
        
        for num in nums[1:]:
            sum1.append(sum1[-1] + num)
            
        for num in reversed(nums[:-1]):
            sum2.append(sum2[-1] + num)
        
        for i in range(0, len(nums)):
            if sum1[i] == sum2[len(nums) - i - 1]:
                return i
        
        return -1
        