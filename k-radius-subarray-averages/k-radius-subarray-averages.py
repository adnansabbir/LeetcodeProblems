class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        average = [-1] * len(nums)
        n = len(nums)

        currSum = sum(nums[:(k*2) + 1])
        for i in range(k, n - k):
            average[i] = currSum // ((k*2) + 1)
            # print(currSum, average, i, i-k, i+k+1)
            if i + k + 1 < n:
                currSum = currSum - nums[i-k] + nums[i+k + 1]
        
        return average
