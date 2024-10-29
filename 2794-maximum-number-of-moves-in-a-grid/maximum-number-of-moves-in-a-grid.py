from functools import lru_cache

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        @lru_cache
        def maxMoveFromPos(row: int, col: int)-> int:
            if col >= len(grid[0]):
                return 0
            
            next_moves = [(row-1, col+1), (row, col+1), (row + 1, col + 1)]
            result = 0
            for next_row, next_col in next_moves:
                if not (0 <= next_row < len(grid) and (0 <= next_col < len(grid[0]))):
                    continue
                if grid[next_row][next_col] > grid[row][col]:
                    result = max(result, maxMoveFromPos(next_row, next_col))
            return result + 1

        result = 0
        for i in range(len(grid)):
            result = max(result, maxMoveFromPos(i,0) - 1)
        return result
        