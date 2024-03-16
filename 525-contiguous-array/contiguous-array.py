class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_index = {0: -1}
        count = 0
        result = 0

        for i, num in enumerate(nums):
            count += 1 if num else -1

            if count not in count_index:
                count_index[count] = i
            else:
                if i - count_index[count] > result:
                    result = i - count_index[count]
        
        return result
