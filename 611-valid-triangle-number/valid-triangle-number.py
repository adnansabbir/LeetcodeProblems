class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for k in range(n-1, 1, -1):
            a, b = 0, k - 1

            while a < b:
                if nums[a] + nums[b] > nums[k]:
                    count += b - a
                    b -= 1
                else:
                    a += 1
        return count

