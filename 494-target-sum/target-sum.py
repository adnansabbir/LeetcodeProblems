from functools import lru_cache 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def exp_count(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            return exp_count(i + 1, total + nums[i]) + exp_count(i + 1, total - nums[i])

        return exp_count(0, 0)
        