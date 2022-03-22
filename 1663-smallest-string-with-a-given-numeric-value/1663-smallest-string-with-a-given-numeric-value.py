class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = [1]*n
        target = k - n
        
        if target == 0:
            return ''.join(['a']*n)
        
        pointer = n-1
        while target:
            result[pointer] = min(target+1, 26)
            target -= (result[pointer] - 1)
            pointer -=1
        
        return ''.join([chr(c + ord('a')-1) for c in result])
                
        