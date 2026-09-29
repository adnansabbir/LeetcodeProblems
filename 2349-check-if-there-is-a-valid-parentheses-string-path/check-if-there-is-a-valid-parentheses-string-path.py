class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        if grid[0][0] != '(' or grid[-1][-1] != ')':
            return False

        rows, cols = len(grid), len(grid[0])

        dp = [[set() for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = {1}

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue

                parent_counts = set()

                if i > 0:
                    parent_counts.update(dp[i - 1][j])

                if j > 0:
                    parent_counts.update(dp[i][j - 1])

                change = 1 if grid[i][j] == '(' else -1

                for count in parent_counts:
                    new_count = count + change

                    if new_count >= 0:
                        dp[i][j].add(new_count)

        return 0 in dp[-1][-1]