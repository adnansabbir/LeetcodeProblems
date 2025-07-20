class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[i==j for j in range(n)] for i in range(n)]
        start, end = 0, 0

        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and (j-i <= 2 or dp[i + 1][j-1])

                if dp[i][j] and j - i > end - start:
                    start, end = i, j
        return s[start:end + 1]