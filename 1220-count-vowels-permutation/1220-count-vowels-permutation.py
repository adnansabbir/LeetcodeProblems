from functools import cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        nextChar = {
            'a': ['e'],
            'e': ['i','a'],
            'i': ['a','e','o','u'],
            'o': ['i','u'],
            'u': ['a']
        }
        maxNum = pow(10,9) + 7
        
        @cache
        def getCombinations(char: str, length: int):
            if length == 1:
                return 1
            
            return sum([getCombinations(ch, length-1) for ch in nextChar[char]])%maxNum
        
        return sum([getCombinations(ch, n) for ch in ['a','e','i','o','u']])%maxNum