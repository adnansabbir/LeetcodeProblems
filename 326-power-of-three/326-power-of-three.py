class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        maxNumber = math.pow(3,19)
        return n>0 and maxNumber%n==0
            
        