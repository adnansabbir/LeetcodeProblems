from functools import lru_cache 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def exp_count(i, total):
            key = f'{i}_{total}'
            if key in cache:
                return cache[key]

            if i == len(nums):
                return 1 if total == target else 0
            
            cache[key] = exp_count(i + 1, total + nums[i]) + exp_count(i + 1, total - nums[i])
            return cache[key]

        return exp_count(0, 0)
        