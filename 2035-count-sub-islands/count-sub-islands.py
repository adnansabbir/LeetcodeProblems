class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid2[row][col] != 1:
                    continue
                
                queue = [(row, col)]
                grid2[row][col] = 0
                is_sub_island = True
                while queue:
                    size = len(queue)
                    for i in range(size):
                        i, j = queue.pop(0)

                        if grid1[i][j] != 1:
                            is_sub_island = False

                        if i != 0 and grid2[i - 1][j] == 1:
                            queue.append((i-1, j))
                            grid2[i-1][j] = 0
                        if i + 1 != len(grid2) and grid2[i + 1][j] == 1:
                            queue.append((i+1, j))
                            grid2[i+1][j] = 0
                        if j != 0 and grid2[i][j - 1] == 1:
                            queue.append((i, j-1))
                            grid2[i][j-1] = 0
                        if j + 1 != len(grid2[0]) and grid2[i][j + 1] == 1:
                            queue.append((i, j + 1))
                            grid2[i][j+1] = 0

                if is_sub_island:
                    result += 1


        return result