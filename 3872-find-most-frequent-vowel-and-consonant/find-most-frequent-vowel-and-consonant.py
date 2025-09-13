class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        freq = {}
        max_vowel, max_conso = 0, 0

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
            if char in vowels:
                max_vowel = max(max_vowel, freq[char])
            else:
                max_conso = max(max_conso, freq[char])
        
        return max_vowel + max_conso
            
        