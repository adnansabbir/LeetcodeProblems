class Solution:
    def longestValidParentheses(self, s: str) -> int:
        d_idx_map = {0: -1}
        depth = 0
        result = 0
        depth_arr = []
        for i, ch in enumerate(s):
            depth += 1 if ch == '(' else -1

            if depth < 0:
                d_idx_map = {0: i}
                depth = 0
            # print(d_idx_map)
            if depth in d_idx_map:
                result = max(result, i - d_idx_map[depth])
                d_idx_map.pop(depth + 1, None)
            else:
                d_idx_map[depth] = i
            depth_arr.append(depth)
        
            # print(depth_arr, result)
        return result
        