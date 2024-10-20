from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)

        result = -1

        for num in nums:
            if freq[num] == 1 and num > result:
                result = num
        
        return result
        