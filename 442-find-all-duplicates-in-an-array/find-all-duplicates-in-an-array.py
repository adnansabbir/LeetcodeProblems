class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        i = 1
        while i <= len(nums):
            currIndex = i - 1
            numInIndex = nums[currIndex]
            swapIndex = numInIndex - 1

            if currIndex == swapIndex:
                i += 1
            elif swapIndex == nums[swapIndex] - 1:
                result.append(numInIndex)
                i += 1
            else:
                nums[swapIndex], nums[currIndex] = numInIndex, nums[swapIndex]

        return [num for i, num in enumerate(nums) if i+1 != num]
