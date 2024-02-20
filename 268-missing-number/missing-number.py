class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingNumber = (len(nums) * (len(nums) + 1))//2

        for num in nums:
            missingNumber -= num

        return missingNumber
        