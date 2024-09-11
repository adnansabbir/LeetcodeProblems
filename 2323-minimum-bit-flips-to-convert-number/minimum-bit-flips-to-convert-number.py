class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        xor = start ^ goal
        while xor:
            result += xor & 1
            xor = xor >> 1
        
        return result
        