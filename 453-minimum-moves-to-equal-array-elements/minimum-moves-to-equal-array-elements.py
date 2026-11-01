from collections import Counter
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # freq, mi, ma = {}, float('inf'), -float('inf')
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        #     mi = min(mi, num)
        #     ma = max(ma, num)

        # keys = sorted(freq.keys())
        # op = 0
        # while len(keys) > 1:
        #     h = keys.pop()
        #     op += freq[h] * (h - keys[-1])
        #     freq[keys[-1]] += freq[h]
            
        # return op

        # In this questions, I realized that we can actaully bring down the largest one by 1 
        # instead of increasing all, saving us O(n)

        # from the above solution we realized that each number eventually comes down to the min
        # and while doing that on each decrement it contributes 1 to the result. 
        # So we can just do it like this 

        mi = min(nums)
        return sum(num - mi for num in nums)