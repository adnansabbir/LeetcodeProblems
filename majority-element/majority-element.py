from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return max(freq.items(), key = lambda x: x[1])[0]