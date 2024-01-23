from functools import lru_cache

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def hasUniqueChars(word: str)-> bool:
            chars = set()
            for ch in word:
                if ch in chars:
                    return False
                chars.add(ch)
            return True

        def mergeAndSort(char1: str, char2: str)-> str:
            return ''.join(sorted(char1 + char2))

        arr = [word for word in arr if hasUniqueChars(word)]
        
        @lru_cache(maxsize=None)
        def getMaxLen(chars: str, idx: int)-> int:
            if idx == len(arr):
                return len(chars)
            
            if not hasUniqueChars(chars + arr[idx]):
                return getMaxLen(chars, idx + 1)

            return max(
                getMaxLen(mergeAndSort(chars, arr[idx]), idx + 1),
                getMaxLen(chars, idx + 1)
            )
        
        return getMaxLen('', 0)
        