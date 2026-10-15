class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        for size in range(1, len(nums) + 1):
            for p in range(len(nums) - size + 1):
                result += len(set(nums[p:p+size]))**2
        return result
        