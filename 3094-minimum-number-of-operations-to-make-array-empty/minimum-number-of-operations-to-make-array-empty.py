from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)

        result = 0
        for num in freq:
            if freq[num] == 1:
                return -1
            
            result += math.ceil(freq[num] / 3)
        return result
        