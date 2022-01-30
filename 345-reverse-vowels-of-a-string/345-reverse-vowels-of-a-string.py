class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        while left<right:
            if s[left] in vowels and s[right] in vowels:
                s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
                left+=1
                right-=1
            
            if s[left] not in vowels:
                left+=1
            
            if s[right] not in vowels:
                right-=1
        
        return s