class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return '0'
        
        if num < 0:
            num += 2**32
        
        hex_map = '0123456789abcdef'
        result = ''
        
        while num:
            result = hex_map[num%16] + result
            num = num//16
            
        return result