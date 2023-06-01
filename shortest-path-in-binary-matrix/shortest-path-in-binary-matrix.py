class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        n = len(grid)
        def getNeighbours(pos: Tuple[int, int]):
            [x, y] = pos
            return [(i, j) for [i, j] in 
                [
                    [x-1, y],
                    [x+1, y],
                    [x, y-1],
                    [x, y + 1],
                    [x - 1, y - 1],
                    [x - 1, y + 1],
                    [x + 1, y - 1],
                    [x + 1, y + 1]
                ]

                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0
            ]
        
        queue = [(0,0)]
        visited = set([(0,0)])
        distance = 1
        while queue:
            size = len(queue)
            for i in range(size):
                [x, y] = queue.pop(0)
                if x == n - 1 and y == n - 1:
                    return distance
                
                for pos in getNeighbours((x, y)):
                    if pos not in visited:
                        visited.add(pos)
                        queue.append(pos)
            distance +=1


        return -1