class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for i in range(1, n):
            if not '0' in (str(i) + str(n-i)):
                return [i, n-i]
        