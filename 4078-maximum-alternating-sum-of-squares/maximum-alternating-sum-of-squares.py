class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x**2)
        largest = 0
        n = len(nums)
        if n % 2:
            largest = nums.pop()
            n -= 1

        result = largest**2
        for i in range(n//2):
            first, second = n - i - 1, i

            result += (nums[first]**2 - nums[second]**2)

        return result