class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]

        maxLen = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    [cSize, cCount] = dp[i]
                    [nSize, nCount] = dp[j]

                    if nSize + 1 > cSize:
                        dp[i] = [nSize + 1, nCount]
                    elif nSize + 1 == cSize:
                        dp[i][1] += nCount
            maxLen = max(maxLen, dp[i][0])
        # print(dp, maxLen)
        return sum([count for [size, count] in dp if size == maxLen])