from collections import Counter
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # [-1,1,3,3]
        # [-1,1,2,2] 1
        # [-1,1,1,1] 2
        # [-1,0,0,0] 3
        # [-1,-1,-1,-1] 3

        # [2,3,3] 2


        freq, mi, ma = {}, float('inf'), -float('inf')
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            mi = min(mi, num)
            ma = max(ma, num)

        keys = sorted(freq.keys())
        op = 0
        while len(keys) > 1:
            h = keys.pop()
            op += freq[h] * (h - keys[-1])
            freq[keys[-1]] += freq[h]
            
        return op