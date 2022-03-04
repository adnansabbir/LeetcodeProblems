class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        stack = [[0]*(n+1) for n in range(query_row+1)]
        
        stack[0][0] = poured
        
        for row in range(query_row):
            for col in range(row+1):
                if stack[row][col] > 1:
                    left = stack[row][col] - 1
                    stack[row+1][col] += left/2
                    stack[row+1][col+1] += left/2
            
        return min(1, stack[query_row][query_glass])
        
        
        