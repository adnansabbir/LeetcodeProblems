class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = b =0
        
        while a<len(s) and b<len(t):
            if s[a] == t[b]:
                a += 1
                b += 1
            else:
                b += 1
        
        return len(s) == a
        