class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        chars = list(s)
        
        while left<right:
            if chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left+=1
                right-=1
            
            if chars[left] not in vowels:
                left+=1
            
            if chars[right] not in vowels:
                right-=1
        
        return ''.join(chars)