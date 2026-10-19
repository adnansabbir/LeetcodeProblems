class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        s_count, t_count = sum(x < target for x in nums), sum(x == target for x in nums)
        return [i for i in range(s_count, s_count + t_count)]
        