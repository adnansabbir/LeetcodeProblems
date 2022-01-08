class Solution:
    dp = {}
    def pick(self, grid: List[List[int]], r, c1, c2):
        if c1 >= len(grid[0]) or c1 < 0:
            return 0
        
        if c2 >= len(grid[0]) or c2 < 0:
            return 0
        
        if r == len(grid)-1:
            return grid[r][c1] + grid[r][c2] if c1 != c2 else grid[r][c1]
        
        key = f'{r}-{c1}-{c2}'
        
        if key in self.dp:
            return self.dp[key]
        
        value = grid[r][c1] + grid[r][c2] if c1 != c2 else grid[r][c1]
        combinations = [
            self.pick(grid, r+1, c1-1, c2-1),
            self.pick(grid, r+1, c1, c2-1),
            self.pick(grid, r+1, c1+1, c2-1),
            self.pick(grid, r+1, c1-1, c2),
            self.pick(grid, r+1, c1, c2),
            self.pick(grid, r+1, c1+1, c2),
            self.pick(grid, r+1, c1-1, c2+1),
            self.pick(grid, r+1, c1, c2+1),
            self.pick(grid, r+1, c1+1, c2+1),
        ]
        
        self.dp[key] = value + max(combinations)
        
        return self.dp[key]
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.dp = {}
        return self.pick(grid, 0, 0, len(grid[0])-1)