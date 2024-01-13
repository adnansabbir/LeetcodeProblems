from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sFreq = Counter(s)

        result = len(s)
        for character in t:
            if character in sFreq and sFreq[character] != 0:
                sFreq[character] -= 1
                result -= 1


        return result