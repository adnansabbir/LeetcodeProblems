class Solution:
    def numSub(self, s: str) -> int:
        count_1 = 0
        s = s + '0'

        result = 0
        for c in s:
            if c == '1':
                count_1 += 1
            else:
                if count_1:
                    result += (count_1 * (count_1 + 1))// 2
                count_1 = 0
        return result % ((10**9) + 7)
            
        