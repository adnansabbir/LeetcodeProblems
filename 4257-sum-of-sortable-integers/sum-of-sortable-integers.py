import math

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:

        def is_sortable(nums, k):
            if k == 1:
                return not sum([nums[i] > nums[i+1] for i in range(len(nums) - 1)])
            last_max = 0
            for i in range(0, len(nums), k):
                bpc = 0
                c_max, c_min = nums[i], nums[i]
                for j in range(i, i+k - 1):
                    bpc += 1 if nums[j] > nums[j+1] else 0
                    c_max, c_min = max(c_max, nums[j+1]), min(c_min, nums[j+1])

                if bpc > 1 or (bpc != 0 and nums[i] < nums[i+k-1]) or c_min < last_max:
                    # print(i, nums[i:i+k], False)
                    return False
                
                # print(i, nums[i:i+k], True)
                last_max = c_max
            return True
                
        n = len(nums)
        ans = 0     
        for i in range(1, n + 1):
            if n % i == 0:
                if yes:= is_sortable(nums, i):
                    ans += i
                print(i, yes)
                # ans += i
        return ans
        