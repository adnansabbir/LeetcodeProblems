class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        length = 0

        for i, c in enumerate(s):
            if c == ' ':
                length = 0
            else:
                length += 1
            
            if length:
                result = length
        
        return result
        