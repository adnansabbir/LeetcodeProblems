class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        cSum = sorted(nums)
        result = -1
        for i in range(1, len(nums)):
            cSum[i] += cSum[i-1]
            if cSum[i] - cSum[i-1] < cSum[i-1]:
                result = cSum[i]


        return result
        