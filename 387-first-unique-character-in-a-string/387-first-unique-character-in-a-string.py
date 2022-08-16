class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = [0]*26
        for ch in s:
            frequency[ord(ch)-ord('a')]+=1
        
        for i, ch in enumerate(s):
            if frequency[ord(ch)-ord('a')] == 1:
                return i
        
        return -1