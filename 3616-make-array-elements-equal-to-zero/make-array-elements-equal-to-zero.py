class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result = 0
        right = sum(nums)
        left = 0

        for num in nums:
            if num == 0:
                if left == right:
                    result += 2
                elif abs(left - right) == 1:
                    result += 1
            right -= num
            left += num
        
        return result
        