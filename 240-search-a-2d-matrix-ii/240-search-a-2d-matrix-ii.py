class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        
        while True:
            if r < 0 or c < 0 or r == len(matrix) or c == len(matrix[0]):
                return False
            
            if target > matrix[r][c]:
                r+=1
            elif target < matrix[r][c]:
                c-=1
            else:
                return True
        