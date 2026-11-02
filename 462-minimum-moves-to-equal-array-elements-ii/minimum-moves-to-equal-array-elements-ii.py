from collections import Counter

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        mi = min(nums)

        op_to_min = sum(num - mi for num in nums)
        op = 0

        freq = Counter(nums)
        keys = sorted(freq.keys(), reverse=True)

        if len(keys) < 2:
            return 0

        left = freq[keys[-1]]
        res = op_to_min
        while len(keys) > 1 and left < len(nums):
            least = keys.pop()

            diff = (keys[-1] - least)
            needed_op = freq[least] * diff
            freq[keys[-1]] += freq[least]

            op += needed_op
            op_to_min -= diff * (len(nums) - left)

            res = min(res, op + op_to_min)
            left += (freq[keys[-1]] - freq[least])

        return res



            
            

        