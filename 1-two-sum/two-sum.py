class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            
            # Add the current number to the map after checking for its complement.
            # This avoids using the same element twice and correctly handles duplicates.
            seen[num] = i
        
        # This part of the code is unreachable given the problem constraint
        # that exactly one valid answer exists.