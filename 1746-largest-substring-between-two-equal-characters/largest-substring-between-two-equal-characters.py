class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lastCharIndex = [-1 for i in range(26)]

        maxSubString = -1

        for i, char in enumerate(s):
            charIndex = ord(char) - ord('a')
            if lastCharIndex[charIndex] == -1:
                lastCharIndex[charIndex] = i
            else:
                maxSubString = max(maxSubString, i - lastCharIndex[charIndex] - 1)
            
        
        return maxSubString

        