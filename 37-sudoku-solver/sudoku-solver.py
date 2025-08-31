class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        triplets = [set() for _ in range(9)]
        empty_pos = []

        def getTripletPos(x, y):
            x_div = x // 3
            y_div = y // 3

            return (x_div * 3) + y_div

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    empty_pos.append((row, col))
                    continue
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                triplets[getTripletPos(row, col)].add(board[row][col])
        
        
        possible_nums = set([str(num) for num in range(1, 10)])
        def solve(idx = 0):
            if idx == len(empty_pos):
                return True
            row, col = empty_pos[idx]
            invalid_nums = rows[row].union(cols[col]).union(triplets[getTripletPos(row, col)])
            valid_nums = list(possible_nums - invalid_nums)
            for num in valid_nums:
                num_str = str(num)
                
                rows[row].add(num)
                cols[col].add(num)
                triplets[getTripletPos(row, col)].add(num)

                if solve(idx + 1):
                    board[row][col] = num
                    return True
                else:
                    rows[row].remove(num)
                    cols[col].remove(num)
                    triplets[getTripletPos(row, col)].remove(num)
            return False
        
        return solve()
                    

        