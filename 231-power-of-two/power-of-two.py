class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        ones = 0
        while n:
            ones += n & 1
            n = n >> 1
        return ones < 2
        