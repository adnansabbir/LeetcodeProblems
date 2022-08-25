class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        frequency = [0]*26
        for c in ransomNote:
            frequency[ord(c)-ord('a')]+=1
        
        charsLeftToCompare = len(ransomNote)
        for c in magazine:
            if frequency[ord(c)-ord('a')]:
                frequency[ord(c)-ord('a')]-=1
                charsLeftToCompare-=1
            
            if not charsLeftToCompare:
                return True
        
        return False