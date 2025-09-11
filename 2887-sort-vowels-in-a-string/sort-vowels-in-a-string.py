class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A','E','I','O','U','a','e','i','o','u'}

        vowel_chars = []
        s_list = list(s)

        for char in s_list:
            if char in vowels:
                vowel_chars.append(char)
        
        vowel_chars.sort()
        for i, char in enumerate(s_list):
            if char in vowels:
                s_list[i] = vowel_chars.pop(0)
        
        return ''.join(s_list)