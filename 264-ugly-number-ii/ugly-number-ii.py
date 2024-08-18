# https://www.youtube.com/watch?v=1pj2a5bmziY

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = i3 = i5 = 0

        for i in range(n):
            next_num = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)

            nums.append(next_num)

            if nums[i2] * 2 == next_num:
                i2 += 1
            if nums[i3] * 3 == next_num:
                i3 += 1
            if nums[i5] * 5 == next_num:
                i5 += 1

        return nums[n-1]
