class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dp = [[[None, None] for __ in range(n)] for _ in range(m)]

        pacific = []
        atlantic = []
        seen_pacific = set()
        seen_atlantic = set()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific.append((i, j))
                    dp[i][j][0] = True
                if i == m-1 or j == n-1:
                    atlantic.append((i, j))
                    dp[i][j][1] = True

        #processing pacific
        while pacific:
            size = len(pacific)
            for _ in range(size):
                px, py = pacific.pop(0)
                
                neighbors = [(px-1,py),(px+1,py),(px,py-1),(px,py+1)]
                for nx, ny in neighbors:
                    if 0 <= nx < m and 0 <= ny < n:
                        if dp[nx][ny][0] == None and heights[nx][ny] >= heights[px][py]:
                            dp[nx][ny][0] = True
                            pacific.append((nx, ny))

        #processing atlantic
        while atlantic:
            size = len(atlantic)
            for _ in range(size):
                ax, ay = atlantic.pop(0)
                
                neighbors = [(ax-1,ay),(ax+1,ay),(ax,ay-1),(ax,ay+1)]
                for nx, ny in neighbors:
                    if 0 <= nx < m and 0 <= ny < n:
                        if dp[nx][ny][1] == None and heights[nx][ny] >= heights[ax][ay]:
                            dp[nx][ny][1] = True
                            atlantic.append((nx, ny))
        
        result = []
        for r in range(m):
            for c in range(n):
                if dp[r][c][0] and dp[r][c][1]:
                    result.append([r, c])

        return result