import math

class Solution:
    def smallestNumber(self, n: int) -> int:
        # print(math.log(n, 2))
        num = int(math.log(n, 2) + 1)
        # print(2**num - 1, bin((2**num) - 1))

        if n == 1:
            return 1
        return (2 ** num) - 1
        