class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        
        count = 0
        
        for c1 in range(n):
            for c2 in range(c1,n):
                sum_map = {0:1}
                cu_sum = 0
                
                for r in range(m):
                    cu_sum += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                    count += sum_map.get(cu_sum - target, 0)
                    sum_map[cu_sum] = sum_map.get(cu_sum, 0) + 1
        return count