class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[0] * c for _ in range(r)]

        def getNeighbours(pos: List[int])-> List[List[int]]:
            x, y = pos
            neighbours = [[x-1, y],[x+1, y], [x, y-1], [x, y + 1]]
            return [[x1, y1] for x1, y1 in neighbours if 0 <= x1 < r and 0 <= y1 < c and grid[x1][y1] > grid[x][y]]
        
        MOD = 10**9 + 7
        def count(pos: List[int])-> int:
            x, y = pos
            if dp[x][y]:
                return dp[x][y]
            
            dp[x][y] = 1
            for nx, ny in getNeighbours([x, y]):
                dp[x][y] += count([nx, ny])
            
            dp[x][y] = dp[x][y] % MOD

            return dp[x][y]

        result = 0
        for i in range(r):
            for j in range(c):
                result += count([i, j])
        return result % MOD