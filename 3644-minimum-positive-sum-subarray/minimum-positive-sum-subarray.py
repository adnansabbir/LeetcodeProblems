class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # 2,5
        # 3,6,-1,-1,7,-8,5,1

        n = len(nums)
        result = []
        for i in range(n-l + 1):
            start, end = i + l, i + r 
            # i = 1, s = 3, e = 6
            ith_sum = sum(nums[i: start])
            min_total = ith_sum
            # can have neg
            for j in range(start, min(n, end)):
                ith_sum += nums[j]
                if ith_sum > 0:
                    if min_total <= 0:
                        min_total = ith_sum
                    else:
                        min_total = min(min_total, ith_sum)
            if min_total > 0:
                result.append(min_total)

        if not result:
            return -1
        return min(result)
        