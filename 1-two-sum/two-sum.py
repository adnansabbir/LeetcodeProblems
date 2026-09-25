class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {nums[0]: 0}

        for i in range(1, len(nums)):
            search_num = target - nums[i]
            if search_num in num_pos:
                return [num_pos[search_num], i]
            else:
                num_pos[nums[i]] = i
        
        return [-1, -1]
        