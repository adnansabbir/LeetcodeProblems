class Solution:
    def checkValidString(self, s: str) -> bool:
        depth_range = [0, 0]
        depth = 0
        for ch in s:
            if ch == '(':
                depth_range[0] += 1
                depth_range[1] += 1
            elif ch == '*':
                depth_range[0] -= 1
                depth_range[1] += 1
            else:
                depth_range[0] -= 1
                depth_range[1] -= 1

            if depth_range[1] < 0:
                return False

            depth_range[0] = max(0, depth_range[0])
            
        return depth_range[0] <= 0 <= depth_range[1] 
        