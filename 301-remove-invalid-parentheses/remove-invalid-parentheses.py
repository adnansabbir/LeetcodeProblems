class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = []
        max_size = 0
        def generate_paranthesises(i = 0, curr = "", depth = 0):
            nonlocal max_size
            if depth < 0:
                return

            if i == len(s):
                if depth == 0:
                    if len(curr) > max_size:
                        max_size = len(curr)
                        result.clear()

                    if len(curr) == max_size:
                        result.append(curr)
                return
            
            c = s[i]
            if c not in {'(', ')'}:
                generate_paranthesises(i + 1, curr + s[i], depth)
            else:
                depth_factor = 1 if c == '(' else -1
                generate_paranthesises(i + 1, curr + s[i], depth + depth_factor)
                generate_paranthesises(i + 1, curr, depth)
        
        generate_paranthesises()
        return list(set(result))