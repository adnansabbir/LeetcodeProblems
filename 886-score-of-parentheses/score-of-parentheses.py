class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # (((()()())))
        # 24
        # ()
        # (
        stack = []
        for ch in s:
            if ch == '(':
                stack.append('(')
            else:
                if stack[-1] == '(':
                    stack.pop()
                    if stack and isinstance(stack[-1], int):
                        stack.append(stack.pop() + 1)
                    else:
                        stack.append(1)
                elif isinstance(stack[-1], int):
                    next_num = stack.pop() * 2
                    stack.pop()
                    stack.append(next_num)
            while len(stack) > 1 and isinstance(stack[-1], int) and isinstance(stack[-2], int):
                stack.append(stack.pop() + stack.pop())
            # print(stack)
        return stack[-1]
        