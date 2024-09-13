class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        result = 0
        for word in words:
            result+= 1
            for char in word:
                if char not in allowed:
                    result -= 1
                    break
            
        return result