class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = ""

        for ch in s:
            if ch == '(':
                if depth != 0:
                    result += ch
                depth += 1
            else:
                if depth != 1:
                    result += ch
                depth -= 1
        return result
        