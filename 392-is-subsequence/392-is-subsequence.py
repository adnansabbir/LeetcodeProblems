class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        s_pointer = 0
        
        for char in t:
            if char == s[s_pointer]:
                s_pointer+=1
            
            if s_pointer == len(s):
                return True
                
        
        return s_pointer == len(s)
        