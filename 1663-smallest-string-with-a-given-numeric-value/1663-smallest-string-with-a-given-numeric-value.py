class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        target = k - n
        
        if target == 0:
            return 'a'*n
        
        result = 'z'* (target//25)
        target = target%25
        
        if target:
            result = chr(target + ord('a')) + result
        
        result = 'a'*(n-len(result)) + result
            
        return result
                
        