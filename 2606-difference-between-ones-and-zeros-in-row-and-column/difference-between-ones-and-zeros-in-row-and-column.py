class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        cache = {}
        m, n = len(grid), len(grid[0])

        def getDiff(row: int, col:int)-> int:
            rowKey = f'r{row}'
            if rowKey not in cache:
                ones = sum(grid[row])
                cache[rowKey] = ones - (n - ones)
            
            colKey = f'c{col}'
            if colKey not in cache:
                cache[colKey] = 0
                for i in range(m):
                    if grid[i][col] == 1:
                        cache[colKey] += 1
                    else:
                        cache[colKey] -= 1
            
            return cache[rowKey] + cache[colKey]
        
        result = [[getDiff(i, j) for j in range(n)] for i in range(m)]
        return result