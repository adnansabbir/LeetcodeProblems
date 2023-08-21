class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, (n//2) + 1):
            pattern = s[:i] * (n//i)
            if pattern == s:
                return True
        return False