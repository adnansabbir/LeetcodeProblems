import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        curr_end, max_distance = 0, 0

        for i in range(n - 1):
            max_distance = max(max_distance, i + nums[i])
            if i == curr_end:
                result += 1
                curr_end = max_distance
        return result

        
