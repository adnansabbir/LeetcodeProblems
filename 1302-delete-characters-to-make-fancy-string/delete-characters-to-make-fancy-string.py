class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ''
        for char in s:
            # print(result, char, len(result), (result[-1] == char and result[-2] == char) if len(result)>2 else True)
            if len(result) < 2 or not (result[-1] == char and result[-2] == char):
                result += char
        
        return result
        