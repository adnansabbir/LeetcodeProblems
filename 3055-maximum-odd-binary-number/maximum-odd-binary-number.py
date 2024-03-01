class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        
        for c in s:
            ones += 1 if c == '1' else 0
        
        return ('1'*(ones -1)) + ('0' * (len(s) - ones)) + '1'
        