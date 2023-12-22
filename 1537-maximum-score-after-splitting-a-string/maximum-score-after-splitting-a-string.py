class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0 if s[0] == '1' else 1
        ones = 0

        for ch in s:
            if ch == '1':
                ones += 1
        
        if s[0] == '1':
            ones -= 1

        result = zeros + ones

        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            result = max(result, zeros + ones)

        return result
        