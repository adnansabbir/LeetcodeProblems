class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            evens = set()
            odds = set()

            if result >= len(nums) - i:
                return result

            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])
                
                if len(evens) == len(odds):
                    result = max(result, j - i + 1)
        return result
                    