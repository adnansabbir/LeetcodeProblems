class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenL = set(brokenLetters)

        result = 0
        brokenFound = 0
        for char in text:
            if char in brokenL:
                brokenFound += 1
            elif char == " ":
                if brokenFound == 0:
                    result += 1
                brokenFound = 0
        
        if brokenFound == 0:
            result += 1
        
        return result
        
