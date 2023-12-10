class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                result[j][i] = num
        return result