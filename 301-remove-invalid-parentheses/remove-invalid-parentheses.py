class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = []
        def generate_paranthesises(i = 0, curr = "", depth = 0):
            if depth == 0:
                result.append(curr)

            if i == len(s) or depth < 0:
                return
            
            c = s[i]
            if c not in {'(', ')'}:
                generate_paranthesises(i + 1, curr + s[i], depth)
            else:
                depth_factor = 1 if c == '(' else -1
                generate_paranthesises(i + 1, curr + s[i], depth + depth_factor)
                generate_paranthesises(i + 1, curr, depth)
        
        generate_paranthesises()
        max_len = max([len(r) for r in result])
        result = list(set([r for r in result if len(r) == max_len]))
        return result