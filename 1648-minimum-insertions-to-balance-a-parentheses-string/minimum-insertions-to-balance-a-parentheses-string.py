class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        normalized = []

        # Pass 1: Normalize closing pairs
        i = 0
        while i < len(s):
            if s[i] == '(':
                normalized.append('(')
            else:
                normalized.append(')')

                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    result += 1

            i += 1

        # Pass 2: Balance parentheses
        depth = 0

        for ch in normalized:
            if ch == '(':
                depth += 1
            else:
                depth -= 1

                if depth < 0:
                    result += 1
                    depth = 0

        return result + depth * 2