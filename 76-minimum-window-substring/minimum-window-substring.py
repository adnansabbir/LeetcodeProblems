from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreq = Counter(t)
        sFreq = {}
        charLeftToBeTaken = len(t)

        l, r = 0, 0
        result = ''
        
        while r < len(s):
            rChar = s[r]
            sFreq[rChar] = sFreq.get(rChar, 0) + 1

            if rChar in tFreq:
                if sFreq[rChar] <= tFreq[rChar]:
                    charLeftToBeTaken -= 1
            while charLeftToBeTaken == 0:
                lChar = s[l]
                
                sFreq[lChar] -= 1
                if lChar in tFreq:
                    if sFreq[lChar] < tFreq[lChar]:
                        if not result:
                            result = s[l:r+1]
                        elif len(result) > (r - l):
                            result = s[l:r+1]
                        charLeftToBeTaken += 1
                l += 1
            r += 1
        return result