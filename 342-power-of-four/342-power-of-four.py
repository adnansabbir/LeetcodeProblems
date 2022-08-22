import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n<1 else math.log(n, 4)%1==0