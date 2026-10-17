class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            res = 0
            while num:
                res += num%10
                num = num // 10
            return res

        digit_sum_and_num = sorted([(get_digit_sum(x), x) for x in nums])
        sorted_num_idx_map = {}
        for i, val in enumerate(digit_sum_and_num):
            sorted_num_idx_map[val[1]] = i

        res = 0
        p = 0
        while p < len(nums):
            num = nums[p]
            if num == digit_sum_and_num[p][1]:
                p += 1
                continue
            
            new_pos = sorted_num_idx_map[num]
            nums[new_pos],nums[p] = nums[p],nums[new_pos]
            res += 1
            # print(p, nums)

        return res
        