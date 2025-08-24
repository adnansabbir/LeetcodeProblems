class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        takenZeroIndex = None
        
        result = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if takenZeroIndex != None:
                    start = takenZeroIndex + 1
                takenZeroIndex = i
            
            result = max(result, i - start)
        
        return result
            
        
        