from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = defaultdict(int)
        
        for c in s:
            s_map[c] +=1
        
        
        for c in t:
            if not s_map[c]:
                return c
            else:
                s_map[c]-=1 