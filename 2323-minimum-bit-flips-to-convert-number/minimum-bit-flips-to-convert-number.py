class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        while start or goal:
            start_rmb = start & 1
            start = start >> 1

            goal_rmb = goal & 1
            goal = goal >> 1

            result += 1 if start_rmb != goal_rmb else 0
        
        return result
        