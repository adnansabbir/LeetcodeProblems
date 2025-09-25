class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []

        for i in range(len(triangle)):
            dp.append([None] * len(triangle[i]))

        for i in range(len(triangle) - 1, 0, -1):
            for j in range(1, len(triangle[i])):
                i_up, j_up = i - 1, j - 1
                triangle[i_up][j_up] += min(triangle[i][j], triangle[i][j-1])
        
        # for l in triangle:
        #     print(l)
        return triangle[0][0]

        
        