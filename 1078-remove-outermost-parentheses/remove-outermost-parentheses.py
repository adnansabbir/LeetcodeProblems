class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = ""

        for ch in s:
            depth += 1 if ch == '(' else -1

            if not ((depth == 1 and ch == '(') or (depth == 0 and ch == ')')):
                result += ch
        return result
        