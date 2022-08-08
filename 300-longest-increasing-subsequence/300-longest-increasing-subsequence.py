from random import randrange
from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def getMaxSubSeq(idx: int)-> int:
            maxLen = 0
            for i in range(idx+1, len(nums)):
                if nums[i] <= nums[idx]: continue
                maxLen = max(maxLen, getMaxSubSeq(i))
            
            return maxLen + 1
        
        # print([randrange(100) for _ in range(200)])
        
        result = max([getMaxSubSeq(i) for i in range(len(nums))])
        return result