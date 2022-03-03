class Solution:
    def getTotalSubSeq(self, length: int)-> int:
        n = length-2
        return (n*(n+1))//2
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        
        nums.append(1000000)
        lastNum = nums[0]
        nums[0] = nums[1] - nums[0]
        
        result = 0
        lastBreakPoint = 0
        
        for i in range(1, len(nums)):
            lastNum, nums[i] = nums[i], nums[i] - lastNum
            
            if nums[i] != nums[i-1]:
                result += self.getTotalSubSeq(i - lastBreakPoint)
                lastBreakPoint = i - 1
        
        return result