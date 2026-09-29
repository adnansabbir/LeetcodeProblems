from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        if grid[0][0] != '(' or grid[-1][-1] != ')':
            return False

        r, c = len(grid), len(grid[0])

        dp = [[set() for i in range(c)] for j in range(r)]
        dp[0][0] = set([1])
        def getParentCount(x, y):
            res = set()
            if x > 0:
                res.update(dp[x-1][y])
            if y > 0:
                res.update(dp[x][y - 1])
            return res
        
        for i in range(r):
            for j in range(c):
                if r == 0 and c == 0:
                    continue
                inc = 1 if grid[i][j] == '(' else -1
                parent_incs = getParentCount(i, j)
                for p_inc in parent_incs:
                    if inc == -1 and p_inc == 0:
                        continue
                    dp[i][j].add(p_inc + inc)
            # print(dp[i])
        
        return 0 in dp[-1][-1]