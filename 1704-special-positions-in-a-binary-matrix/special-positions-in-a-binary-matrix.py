class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cache = {}
        m, n = len(mat), len(mat[0])

        def isSpecial(row: int, col:int)-> int:
            if mat[row][col] != 1:
                return 0

            rowKey = f'r{row}'
            if rowKey not in cache:
                cache[rowKey] = sum(mat[row])
            
            colKey = f'c{col}'
            if colKey not in cache:
                cache[colKey] = 0
                for i in range(len(mat)):
                    cache[colKey] += mat[i][col]
            
            return 1 if (cache[rowKey] + cache[colKey] - mat[row][col]) == 1 else 0
        
        result = sum(isSpecial(i, j) for j in range(n) for i in range(m))

        # for num in ([i,j, isSpecial(i, j)] for j in range(n) for i in range(m)):
        #     print(num)
        return result
        