class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x**2)

        # [1,2,3,4,5]
        # 5 - 1 + 4 - 2 + 3 
        # shift largest to the end for odd
        # 4 - 1 + 3 - 2 + 5

        # [1,2,3,4]
        # for even
        # 4 - 1 + 3 - 2

        # 4 - 1 + 3 - 3


        largest = 0
        n = len(nums)
        if n % 2:
            largest = nums.pop()
            n -= 1

        result = largest**2
        for i in range(n//2):
            first, second = n - i - 1, i

            result += nums[first]**2
            result -= nums[second]**2

        return result