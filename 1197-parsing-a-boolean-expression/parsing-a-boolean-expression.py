class Solution:
    def evaluate(self, logic: str, expr: List[str])-> bool:
        if logic == '!':
            return not expr[0]
        elif logic == '&':
            return all(expr)
        elif logic == '|':
            return any(expr)

    def parseBoolExpr(self, expression: str) -> bool:
        lastLogic = []
        stack = []
        current_expr = []
        
        for char in expression:
            if char in ['!', '&', '|']:
                lastLogic.append(char)
            elif char in ['(', 't', 'f']:
                if char == 't':
                    stack.append(True)
                elif char == 'f':
                    stack.append(False)
                else:
                    stack.append(char)

            elif char == ')':
                ce_char = stack.pop()
                while ce_char != '(':
                    current_expr.append(ce_char)
                    ce_char = stack.pop()
                stack.append(self.evaluate(lastLogic.pop(), current_expr))
                current_expr = []

        return stack[0]
        