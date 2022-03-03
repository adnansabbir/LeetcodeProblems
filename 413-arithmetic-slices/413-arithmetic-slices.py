class Solution:
    def getTotalSubSeq(self, length: int)-> int:
        n = length-2
        return (n*(n+1))//2
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        
        if len(nums)<3:
            return result
        
        prev_diff = nums[1] - nums[0]
        
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff != prev_diff:
                return self.getTotalSubSeq(i) + self.numberOfArithmeticSlices(nums[i-1:])
            
            result = self.getTotalSubSeq(i+1)
        
        return result