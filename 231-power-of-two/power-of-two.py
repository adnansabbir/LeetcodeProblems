class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n:
            if n > 1 and n & 1:
                return False
            n = n >> 1
        return True
        