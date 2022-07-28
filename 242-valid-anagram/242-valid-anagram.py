class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequencies = [0]*26
        
        for ch in s:
            frequencies[ord(ch) - ord('a')] += 1
        
        for ch in t:
            frequencies[ord(ch) - ord('a')] -= 1
            if frequencies[ord(ch) - ord('a')] < 0:
                return False
        
        return True
        