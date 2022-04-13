class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for _ in range(n)]
        
        def fillOuter(val: int, start: int)-> int:
            x = y = start
            
            for i in range(y, n-y):
                result[x][i] = val
                val+=1
            
            for i in range(x+1, n-x-1):
                result[i][n-y-1] = val
                val+=1
            
            for i in reversed(range(y, n-y)):
                result[n-x-1][i] = val
                val+=1
            
            for i in reversed(range(x+1, n-x-1)):
                result[i][y] = val
                val+=1
                
            return val
        
        currVal = 1
        for i in range(n//2):
            currVal = fillOuter(currVal, i)
        
        if n%2:
            result[n//2][n//2] =  currVal
        
        return result
        