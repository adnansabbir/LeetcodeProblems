class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            if num % 3 == 1 or num% 3 == 2:
                result += 1
        return result 

        