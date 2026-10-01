class Solution:
    def isValid(self, s: str) -> bool:
        brakets = []
        cl_bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
            }
        for char in s:
            if char in {'(', '{', '['}:
                brakets.append(char)
            elif brakets and cl_bracket_map.get(char) == brakets[-1]:
                brakets.pop()
            else:
                return False
        
        return not brakets

