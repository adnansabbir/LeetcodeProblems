class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCharMap = {}
        mappedCharOfT = set()

        for i, char in enumerate(s):
            if char not in sCharMap:
                if t[i] in mappedCharOfT:
                    return False
                
                sCharMap[char] = t[i]
                mappedCharOfT.add(t[i])
            elif sCharMap[char] != t[i]:
                return False

        return True