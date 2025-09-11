class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A','E','I','O','U','a','e','i','o','u'}

        vowel_chars = {}
        s_list = list(s)

        for char in s_list:
            if char in vowels:
                vowel_chars[char] = vowel_chars.get(char, 0) + 1
        
        vowels_list = sorted(list(vowel_chars.keys()))
        for i, char in enumerate(s_list):
            if char in vowels:
                ch = vowels_list[0]
                s_list[i] = ch

                vowel_chars[ch] -= 1
                if vowel_chars[ch] == 0:
                    vowels_list.pop(0)
        
        return ''.join(s_list)