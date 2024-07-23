from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = sorted([(count, num) for num, count in Counter(nums).items()], key = lambda x: (x[0], -x[1]))
        result = []
        for count, num in freq:
            result += [num] * count
        return result
        