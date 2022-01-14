class Solution:
    def checkString(self, s: str) -> bool:
        a_start = 0
        
        while a_start<len(s) and s[a_start] == 'a':
            a_start +=1
        
        while a_start < len(s):
            if s[a_start] == 'a':
                return False
            
            a_start+=1
        
        return True