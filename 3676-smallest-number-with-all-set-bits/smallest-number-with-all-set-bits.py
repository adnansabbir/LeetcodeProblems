import math

class Solution:
    def smallestNumber(self, n: int) -> int:
        num = int(math.log(n, 2) + 1)
        return (2 ** num) - 1
        