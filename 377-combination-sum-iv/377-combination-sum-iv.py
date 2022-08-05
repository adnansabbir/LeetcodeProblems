from functools import cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def count(targetLeft: int)-> int:

            if targetLeft == 0:
                return 1
            
            if targetLeft<0:
                return 0
            
            return sum([count(targetLeft - num) for num in nums])
        
        result = count(target)
        return result