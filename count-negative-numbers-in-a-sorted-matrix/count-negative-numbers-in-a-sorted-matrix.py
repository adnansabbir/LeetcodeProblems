class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for row in grid:
            for num in row:
                if num < 0:
                    result += 1
        
        return result 