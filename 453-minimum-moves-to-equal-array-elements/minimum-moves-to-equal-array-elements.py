from collections import Counter
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mi = min(nums)
        return sum([num - mi for num in nums])