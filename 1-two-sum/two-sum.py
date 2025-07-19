class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            target_rem = target - num
            if target_rem in seen:
                return [seen[target_rem], i]
            
            if num not in seen:
                seen[num] = i
        
        return []