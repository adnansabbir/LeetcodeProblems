class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        depth = 0

        for ch in s:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            result = max(result, depth)
            
        return result
        