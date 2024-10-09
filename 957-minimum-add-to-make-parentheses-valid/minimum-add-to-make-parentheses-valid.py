class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # look for missing closing paranthesis
        stack = []

        for char in s:
            if char == '(':
                stack.append(')')
            elif char == ')':
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    stack.append('(')

        return len(stack)
        