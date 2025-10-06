class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        dp = [[None]*n for _ in range(n)]
        dp[0][0] = grid[0][0]
        
        q = [(0, 0, grid[0][0])]

        while q:
            size = len(q)
            for _ in range(size):
                cx, cy, c_val = q.pop(0)
                for x, y in [(cx+1, cy), (cx-1, cy),(cx, cy+1), (cx, cy-1)]:
                    if not (0 <= x < n) or not (0 <= y < n):
                        continue
                    val = max(c_val, grid[x][y])
                    if dp[x][y] == None or dp[x][y] > val:
                        dp[x][y] = val
                        q.append((x, y, val))

        return dp[-1][-1]