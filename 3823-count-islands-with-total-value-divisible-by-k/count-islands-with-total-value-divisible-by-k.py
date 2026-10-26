class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def get_island_sum_and_mark_zero(x, y):
            total = grid[x][y]
            grid[x][y] = 0
            q = [(x, y)]

            while q:
                cx, cy = q.pop()

                for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > 0:
                        # print(nx, ny, grid[nx][ny])
                        total += grid[nx][ny]
                        grid[nx][ny] = 0
                        q.append((nx, ny))
            return total
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    # print(grid[i][j], i, j)
                    t = get_island_sum_and_mark_zero(i, j)
                    # print(t)
                    # print('\n')
                    if t % k == 0:
                        ans += 1

        return ans

        # [
        # [0,   0,  0]
        # [0,   0,  1]
        # [11,  0,  6]
        # [0,   10, 2]
        # [0,   0,  0]
        # [8,   0,  0]
        # ]