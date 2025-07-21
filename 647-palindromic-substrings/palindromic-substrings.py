class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        # iterate for odd combi
        for i in range(len(s)):
            start, end = i, i

            while start >= 0 and end < len(s) and s[start] == s[end]:
                result += 1
                start -= 1
                end += 1
        # iterate for even combi
        for i in range(1, len(s)):
            start, end = i-1, i

            while start >= 0 and end < len(s) and s[start] == s[end]:
                result += 1
                start -= 1
                end += 1
        return result