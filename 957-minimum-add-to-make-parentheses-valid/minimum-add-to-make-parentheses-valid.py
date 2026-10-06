class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result = 0
        depth = 0
        for ch in s:
            depth += 1 if ch == '(' else -1

            if depth < 0:
                result += -depth
                depth = 0
        
        return result + depth