class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            if not n % (i+1):
                result += nums[i]**2

        return result