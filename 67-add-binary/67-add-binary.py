class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b = '0'*(len(a)-len(b))+b
        if len(a)<len(b):
            a = '0'*(len(b)-len(a))+a
        
        carry = 0
        result = ''
        for i in reversed(range(len(a))):
            total = int(a[i]) + int(b[i]) + carry
            
            if total == 2:
                carry = 1
                total = 0
            elif total == 3:
                carry = 1
                total = 1
            elif total == 1:
                carry = 0
                
            result = f'{total}{result}'
        
        if carry == 1:
            result = f'{carry}{result}'
        return result