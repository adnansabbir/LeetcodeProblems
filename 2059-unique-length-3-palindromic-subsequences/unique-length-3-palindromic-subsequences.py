from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        result = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])
            
            result += len(between)
        return result