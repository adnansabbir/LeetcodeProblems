class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in text2] for i in text1]

        def getDpValue(i: int, j: int)-> int:
            return dp[i][j] if 0 <= i < len(text1) and 0 <= j < len(text2) else 0

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = getDpValue(i-1, j-1) + 1
                else:
                    dp[i][j] = max(getDpValue(i, j - 1), getDpValue(i - 1, j))

        return dp[-1][-1]
        