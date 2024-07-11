class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                # take all out till opening
                # reverse
                # put back
                temp_str = ''
                while stack[-1] != '(':
                    temp_str += stack.pop()
                stack.pop()
                # print(temp_str)
                for letter in temp_str:
                    stack.append(letter)
            else:
                stack.append(char)
            
            # print(stack)
        
        return ''.join(stack)