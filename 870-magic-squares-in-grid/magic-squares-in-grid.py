class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        nums_in_square = []

        def print_magic():
            for row in nums_in_square:
                print(row)
            print('\n')

        def is_magic_square(grid):
            # Check if grid is 3x3
            if len(grid) != 3 or any(len(row) != 3 for row in grid):
                return False

            # Check if all numbers from 1 to 9 are present
            numbers = set(num for row in grid for num in row)
            if numbers != set(range(1, 10)):
                return False

            # Calculate the sum of the first row to compare with others
            magic_sum = sum(grid[0])

            # Check sum of each row
            for row in grid:
                if sum(row) != magic_sum:
                    return False

            # Check sum of each column
            for col in range(3):
                if sum(grid[row][col] for row in range(3)) != magic_sum:
                    return False

            # Check sum of the diagonals
            if sum(grid[i][i] for i in range(3)) != magic_sum:
                return False

            if sum(grid[i][2 - i] for i in range(3)) != magic_sum:
                return False

            return True

        result = 0
        for i in range(3):
            if len(nums_in_square) <= i:
                nums_in_square.append([])
            for j in range(3):
                nums_in_square[i].append(grid[i][j])
        
        result += is_magic_square(nums_in_square)

        def update_magic_square(nums: list[int], right = True):
            print(nums, right)
            if right:
                for row in nums_in_square:
                    row.pop(0)
                    row.append(nums.pop(0))
            else:
                nums_in_square.pop(0)
                nums_in_square.append(nums)

        for i in range(2, len(grid)):
            # from next iteration
            if i > 2:
                print('Going Down')
                update_magic_square([grid[i][0], grid[i][1], grid[i][2]], False)
                result += is_magic_square(nums_in_square)

            temp_num_in_square = [row.copy() for row in nums_in_square]
            for j in range(3, len(grid[0])):
                print('Going right')
                update_magic_square([grid[i-2][j], grid[i-1][j], grid[i][j]])
                result += is_magic_square(nums_in_square)
            nums_in_square = temp_num_in_square

        
        return result


        