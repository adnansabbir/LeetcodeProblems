class Solution:
    def minLength(self, s: str) -> int:
        last_len = len(s)
        s = s.replace('AB', '')
        s = s.replace('CD', '')

        while last_len != len(s):
            last_len = len(s)
            s = s.replace('AB', '')
            s = s.replace('CD', '')

        return len(s)
        