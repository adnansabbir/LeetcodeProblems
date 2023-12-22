class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == '0' else 0
        ones = sum([1 for ch in s[1:] if ch == '1'])
        
        result = zeros + ones

        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            
            result = max(result, zeros + ones)
        
        return result