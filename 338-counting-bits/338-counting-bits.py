class Solution:
    def getNoOf1Bits(self, num: int)-> int:
        count = 0
        while num:
            count += num&1
            num>>=1
        return count
    
    def countBits(self, n: int) -> List[int]:
        return [self.getNoOf1Bits(i) for i in range(n+1)]