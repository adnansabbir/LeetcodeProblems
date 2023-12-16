from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sFreq = dict(Counter(s))
        for c in t:
            if c in sFreq and sFreq[c] > 0:
                sFreq[c] -= 1
            else:
                return False
        return True
        