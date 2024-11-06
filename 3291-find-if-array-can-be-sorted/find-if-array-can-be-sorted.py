from functools import lru_cache
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        @lru_cache
        def get_bit_count(num) -> int:
            result = 0
            while num:
                result += num & 1
                num = num >> 1
            return result
        
        for i, curr in enumerate(nums):
            for j, prev in enumerate(nums[:i]):
                if curr < prev and get_bit_count(curr) != get_bit_count(prev):
                    return False
        return True

        