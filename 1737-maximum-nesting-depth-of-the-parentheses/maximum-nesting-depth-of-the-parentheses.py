class Solution:
    def maxDepth(self, s: str) -> int:
        result, depth = 0, 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            result = max(result, depth)

        return result
        