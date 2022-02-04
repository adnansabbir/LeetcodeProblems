class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_sub = 0
        hash_count = {0: -1}
        count = 0

        for i, num in enumerate(nums):
            count = count + 1 if num else count - 1
            if count not in hash_count:
                hash_count[count] = i
            elif i - hash_count[count] > max_sub:
                max_sub = i - hash_count[count]

        return max_sub