class Solution:
    def maxOperations(self, s: str) -> int:
        s = s.rstrip('1')
        
        result, ones = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                continue
            
            if s[i+1] == '0':
                result += (1 + ones)
                ones += 1
            else:
                result += ones

        return result

            
