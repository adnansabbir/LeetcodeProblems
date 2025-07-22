from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def isWordInDict(start)-> bool:
            for e in range(start + 1, len(s) + 1):
                word = s[start:e]
                if word in wordDict and isWordInDict(e):
                    return True
            return start >= len(s)
        
        return isWordInDict(0)

        