from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)

        def countMinOperation(freq: int) -> int:
            if freq < 2:
                return -1
            return math.ceil(freq / 3)

        result = 0
        for num in freq:
            if freq[num] == 1:
                return -1
            
            result += countMinOperation(freq[num])
        return result
        