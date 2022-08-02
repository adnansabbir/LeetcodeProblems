class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])
                
        arr.sort()
        return arr[k-1]
        