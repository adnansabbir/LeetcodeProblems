class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sortDiagonal(x:int, y:int):
            s,e = x,y
            arr = []
            while x<len(mat) and y<len(mat[0]):
                arr.append(mat[x][y])
                x+=1
                y+=1
            arr.sort()
            x -=1
            y -=1
            
            while x>=0 and y>=0:
                mat[x][y] = arr.pop()
                x-=1
                y-=1
        
        for i in range(len(mat)):
            sortDiagonal(i,0)
        
        for j in range(1, len(mat[0])):
            sortDiagonal(0,j)
            
        return mat