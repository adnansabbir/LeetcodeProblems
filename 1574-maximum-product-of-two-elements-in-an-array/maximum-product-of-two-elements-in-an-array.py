class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return (nums[0] - 1) * (nums[1] - 1)

        highestIndex = 0
        secondHighestIndex = 0

        for i, num in enumerate(nums):
            if num > nums[highestIndex]:
                highestIndex = i

        if highestIndex == 0:
            secondHighestIndex = 1

        for i, num in enumerate(nums):
            if num > nums[secondHighestIndex] and i != highestIndex:
                secondHighestIndex = i
        print(highestIndex, secondHighestIndex)

        return (nums[highestIndex] - 1 ) * (nums[secondHighestIndex] - 1 )
        