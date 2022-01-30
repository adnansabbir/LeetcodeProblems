class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            num = sum([int(d) for d in str(num)])
        return num            
        