class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        end_occur = {}
        stack = []
        stack_trace = set()
        
        for i, c in enumerate(s):
            end_occur[c] = i
            
        for i, c in enumerate(s):
            if c not in stack_trace:
                while stack and stack[-1] > c and end_occur[stack[-1]] > i:
                    stack_trace.remove(stack.pop())
                
                stack.append(c)
                stack_trace.add(c)
        
        return "".join(stack)