class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(c) for c in s]

        n = len(nums)
        while n > 2:
            for i in range(1, n):
                nums[i-1] = (nums[i-1] + nums[i]) %10
            n-=1

        return nums[0] == nums[1]