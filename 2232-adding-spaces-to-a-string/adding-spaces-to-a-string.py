class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []

        for i in range(len(s)):
            if spaces and i == spaces[0]:
                result.append(' ')
                spaces.pop(0)
            
            result.append(s[i])
        return ''.join(result)