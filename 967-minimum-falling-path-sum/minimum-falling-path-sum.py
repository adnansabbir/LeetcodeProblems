class Solution:
    def minFallingPathSum(self, cost):
        
        def getValue(i: int, j: int)-> int:
            if 0 <= i < len(cost) and 0 <= j < len(cost[0]):
                return cost[i][j]
            
            return 99999999

        for i in range(1, len(cost)):
            for j in range(0, len(cost[0])):
                print(i,j, cost[i][j], min(getValue(i-1, j-1), getValue(i-1, j), getValue(i-1, j+1)))
                cost[i][j] += min(getValue(i-1, j-1), getValue(i-1, j), getValue(i-1, j+1))
        
        return min(cost[-1])
