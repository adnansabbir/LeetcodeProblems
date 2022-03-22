class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ''
        target = k - n
        
        if target == 0:
            while n:
                result+='a'
                n-=1
        
        while target >= 25:
            result = 'z' + result
            target -= 25
        
        if target:
            result = chr(target + ord('a')) + result
        while len(result) < n:
            result = 'a' + result
        # while target:
        #     if target == 25:
        #         result = 'z' + result
        #         target -= 25
        #     elif target > 25:
        #         result = 'z' + result
        #         target -=25
        #     else:
        #         result = chr(target + ord('a')) + result
        #         target = 0
        
        # while len(result)<n:
        #     result = 'a' + result
            
        return result
                
        