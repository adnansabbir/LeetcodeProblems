class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        s_count, t_count = len([x for x in nums if x < target]), len([x for x in nums if x == target])
        return [i for i in range(s_count, s_count + t_count)]
        