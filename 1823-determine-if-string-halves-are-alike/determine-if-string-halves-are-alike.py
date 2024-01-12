class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aAeEiIoOuU')

        vowelsInFirstHalf = 0
        vowelsInSecondHalf = 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                vowelsInFirstHalf += 1
            if s[len(s) - i - 1] in vowels:
                vowelsInSecondHalf += 1
        
        return vowelsInFirstHalf == vowelsInSecondHalf
        