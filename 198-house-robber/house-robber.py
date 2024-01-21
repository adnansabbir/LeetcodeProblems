from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache(maxsize=None)
        def getMaxSum(idx: int, skip: bool)-> int:
            if idx == len(nums):
                return 0
            
            if skip:
                return getMaxSum(idx + 1, False)
            
            return max(
                nums[idx] + getMaxSum(idx + 1, True),
                getMaxSum(idx + 1, False)
            )

        return getMaxSum(0, False)


        