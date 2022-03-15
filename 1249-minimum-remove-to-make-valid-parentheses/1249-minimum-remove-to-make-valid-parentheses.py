class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pointer = 0
        count = 0
        
        while pointer < len(s):
            if s[pointer] == '(':
                count +=1
            elif s[pointer] == ')':
                count -=1
            
            if count<0:
                s = s[:pointer]+s[pointer+1:]
                pointer -= 1
                count +=1
                
            pointer += 1
        
        result = ''
        
        for i in reversed(range(len(s))):
            if s[i] == '(' and count:
                count -=1
            else:
                result = s[i] + result
                
            
        
        return result