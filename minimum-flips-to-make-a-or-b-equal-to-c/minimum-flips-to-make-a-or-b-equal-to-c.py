class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        while a or b or c:
            aRight, bRight, cRight = a & 1, b & 1, c & 1
            # print(bin(a), aRight, bin(b), bRight, bin(c), cRight)
            a, b, c = a >> 1, b >> 1, c >> 1

            if aRight | bRight == cRight:
                continue
            
            # 1 == 0 | 0
            # 0 == 1 | 0, 0 | 1, 1|1
            if cRight:
                result += 1
            else:
                result += (aRight + bRight)

        return result