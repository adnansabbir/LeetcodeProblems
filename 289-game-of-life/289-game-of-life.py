class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 10 --> 1 -> 0
        # 2 --> 0 -> 1
        val_map = {
            0: 0,
            1: 1,
            10: 1,
            2: 0
        }
        val_map_rev = {
            0: 0,
            1: 1,
            10: 0,
            2: 1
        }
        
        def nextState(x: int, y: int)-> int:
            total = 0
            up = x > 0
            down = x < len(board) - 1
            left = y > 0
            right = y < len(board[0]) - 1
            
            if up:
                total += val_map[board[x-1][y]]
            
            if down:
                total += val_map[board[x+1][y]]
            
            if left:
                total += val_map[board[x][y-1]]
            
            if right:
                total += val_map[board[x][y+1]]
            
            if up and left:
                total += val_map[board[x-1][y-1]]
            
            if down and right:
                total += val_map[board[x+1][y+1]]
            
            if up and right:
                total += val_map[board[x-1][y+1]]
            
            if down and left:
                total += val_map[board[x+1][y-1]]
            
            if total < 2:
                return 10 if board[x][y] else 0
            elif total == 3:
                return board[x][y] if board[x][y] else 2
            elif 1 < total < 4:
                return board[x][y]
            elif total > 3:
                return 10 if board[x][y] else 0
            
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = nextState(x, y)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = val_map_rev[board[x][y]]
        
        