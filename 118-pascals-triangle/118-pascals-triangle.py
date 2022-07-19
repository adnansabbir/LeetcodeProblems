class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        def getVal(x,y)-> int:
            return 0 if (y < 0 or y==len(result[x])) else result[x][y]
        
        for i in range(2, numRows + 1):
            res = []
            for j in range(i):
                res.append(getVal(i-2, j-1) + getVal(i-2, j))
            result.append(res)
            
        return result