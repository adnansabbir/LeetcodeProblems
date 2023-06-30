class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
         
        filledOnDay = [[None]*col for r in range(row)]
        for i, [r,c] in enumerate(cells):
            filledOnDay[r-1][c-1] = i+1
        
        def getNeighbours(pos: Tuple[int], currDay: int, visited: set)-> List[Tuple[int]]:
            [r, c] = pos
            neighbour = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            return [(x, y) for [x, y] in neighbour if 0 <= x < row and 0 <= y < col and (x, y) not in visited and filledOnDay[x][y] > currDay]

        def canReachBottom(currDay: int)-> bool:
            queue = [(0, c) for c in range(col) if filledOnDay[0][c] > currDay]
            visited = set(queue)
            while queue:
                size = len(queue)
                for _ in range(size):
                    [r, c] = queue.pop(0)
                    if r == row - 1:
                        return True
                    
                    neighbours = getNeighbours((r,c), currDay, visited)
                    for neigh in neighbours:
                        visited.add(neigh)
                        queue.append(neigh)
                    # queue = queue + neighbours
            return False
        
        start, end = 0, len(cells)
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if canReachBottom(mid):
                result = max(result, mid)
                start = mid + 1
            else:
                end = mid - 1
        return result