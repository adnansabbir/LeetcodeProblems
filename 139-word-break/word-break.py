from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)

        @lru_cache(maxsize=None)
        def canBreakWord(word: str)-> bool:
            if word in wordDictSet:
                return True
            
            if len(word) < 2:
                return False
            
            for i in range(1, len(word), 1):
                # print(f'{word} : {word[:i]} {word[i:]}')
                if canBreakWord(word[:i]) and canBreakWord(word[i:]):
                    return True
            
            return False
        
        return canBreakWord(s)