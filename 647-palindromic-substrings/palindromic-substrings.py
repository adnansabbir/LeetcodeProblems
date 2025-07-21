class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = n
        dp = [[i==j for j in range(n)] for i in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1])
                result += 1 if dp[i][j] else 0
        return result