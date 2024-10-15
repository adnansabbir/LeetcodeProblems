class Solution:
    def minimumSteps(self, s: str) -> int:
        leftpos = 0
        result = 0
        for i, char in enumerate(s):
            if char == '0':
                result += i - leftpos
                leftpos+= 1

        return result
        