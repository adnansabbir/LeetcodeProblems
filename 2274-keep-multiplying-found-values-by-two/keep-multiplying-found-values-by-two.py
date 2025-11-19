class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        result = original
        nums_set = set(nums)

        while original in nums_set:
            result += original
            original = original * 2
        
        return result 
        