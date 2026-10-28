class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for j in range(n)] for i in range(m)] 
        # dp[0][0].add(grid[0][0])
        # for d in dp:
        #     print(d)

        def get_dp_val(x, y):
            if 0 <= x < m and 0 <= y < n:
                return dp[x][y]
            return set()

        for i in range(m):
            for j in range(n):
                top_left = get_dp_val(i-1, j) | get_dp_val(i, j - 1)
                if not top_left:
                    dp[i][j].add(grid[i][j])
                for num in top_left:
                    dp[i][j].add(num ^ grid[i][j])


        return min(dp[-1][-1])
        # res = float('inf')
        # while q:
        #     cx, cy, val = q.pop(0)

        #     if cx == m - 1 and cy == n - 1:
        #         res = min(res, val)
        #         # print(cx, cy, val)
        #         continue

        #     for nx, ny in [(cx+1, cy), (cx, cy + 1)]:
        #         if 0 <= nx < m and 0 <= ny < n:
        #             q.append((nx, ny, val^grid[nx][ny])) 
        # return res