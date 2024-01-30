class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: y - x,
            '*': lambda x, y: x * y,
            '/': lambda x, y: y // x if y / x >= 0 else (abs(y) // abs(x)) * -1
        }
        
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                stack.append(operations[token](stack.pop(), stack.pop()))

        return floor(stack[0])