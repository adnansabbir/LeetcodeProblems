class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        number = 0
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
                continue
                
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
        
        return stack[0]