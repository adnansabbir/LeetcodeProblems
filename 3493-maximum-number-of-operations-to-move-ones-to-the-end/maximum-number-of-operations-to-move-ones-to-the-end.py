class Solution:
    def maxOperations(self, s: str) -> int:
        s = s.rstrip('1')
        has_zero_after = True
        count_1 = 0
        result = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] != '1':
                has_zero_after = True
                continue
            
            result += ((1 if has_zero_after else 0) + count_1)
            if has_zero_after:
                count_1 += 1
            has_zero_after = False
            
        return result

            
