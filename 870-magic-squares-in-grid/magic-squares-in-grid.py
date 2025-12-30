class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_grid(x1:int, y1:int, x2: int, y2:int)-> bool:
            uniq = set()
            r_sums, c_sums, diag_sum = [0,0,0], [0,0,0], [0,0]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    # uniq check
                    if grid[i][j] in uniq or grid[i][j] > 9 or grid[i][j] < 1:
                        return False
                    else:
                        uniq.add(grid[i][j])

                    r,c = i - x1, j - y1
                    # row col sum
                    r_sums[r] += grid[i][j]
                    c_sums[c] += grid[i][j]

                    # tl to rb diag sum
                    if r == c:
                        diag_sum[0] += grid[i][j]

                    # tr to lb diag sum
                    if (r == 0 and c == 2) or (r == 1 and c == 1) or (r == 2 and c == 0):
                        diag_sum[1] += grid[i][j]

            return r_sums[0] == r_sums[1] and r_sums[0] == r_sums[2] and r_sums[0] == c_sums[0] and r_sums[0] == c_sums[1] and r_sums[0] == c_sums[2] and r_sums[0] == diag_sum[0] and r_sums[0] == diag_sum[1]

        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m-2):
            for j in range(n - 2):
                if is_magic_grid(i,j, i+3, j+3):
                    result += 1
        
        return result
        