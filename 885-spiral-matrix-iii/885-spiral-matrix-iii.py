class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        moves = [1, 1, 2, 2]
        [rPos, cPos] = [rStart, cStart]
        
        result = []
        while len(result) < (rows * cols):
            for i in range(moves[0]):
                if 0 <= rPos < rows and 0 <= cPos < cols:
                    result.append([rPos, cPos])
                cPos+=1

            for i in range(moves[1]):
                if 0 <= rPos < rows and 0 <= cPos < cols:
                    result.append([rPos, cPos])
                rPos+=1

            for i in range(moves[2]):
                if 0 <= rPos < rows and 0 <= cPos < cols:
                    result.append([rPos, cPos])
                cPos-=1

            for i in range(moves[3]):
                if 0 <= rPos < rows and 0 <= cPos < cols:
                    result.append([rPos, cPos])
                rPos-=1
            
            moves[0] += 2
            moves[1] += 2
            moves[2] = moves[0] + 1
            moves[3] = moves[1] + 1
            
        return result
            
        
        