class Solution:
    def longestValidParentheses(self, s: str) -> int:
        d_idx_map = [-1]
        result = 0
        for i, ch in enumerate(s):
            if ch == '(':
                d_idx_map.append(i)
            elif len(d_idx_map) == 1:
                # Eliminating ) at the beginning 
                d_idx_map[0] = i
            else:
                d_idx_map.pop()
                result = max(result, i - d_idx_map[-1])
        return result
        