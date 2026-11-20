class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        for key, val in count.items():
            if val == 1:
                return key