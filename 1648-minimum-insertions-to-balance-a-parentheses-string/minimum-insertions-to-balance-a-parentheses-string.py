import math

class Solution:
    def minInsertions(self, s: str) -> int:
        s += '('
        result = 0
        p = 0
        depth = 0

        while p < len(s):
            if s[p] == '(':
                if depth < 0:
                    o_needed =  math.ceil(-depth)
                    c_needed = (o_needed + depth) * 2
                    result += (o_needed + c_needed)
                    depth = 0
                elif depth % 1 == 0.5:
                    depth -= 0.5
                    result += 1
                depth += 1
            else:
                depth -= 0.5
            p += 1
        
        depth -= 1
        if depth > 0:
            result += depth * 2
        return int(result)
        