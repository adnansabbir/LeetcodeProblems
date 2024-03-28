class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charMap = {}
        mappedCharOfT = set()
        
        for i, char in enumerate(s):
            if s[i] not in charMap:
                if t[i] in mappedCharOfT:
                    return False
                else:
                    charMap[s[i]] = t[i]
                    mappedCharOfT.add(t[i])

            elif t[i] != charMap[s[i]]:
                return False
        
        return True