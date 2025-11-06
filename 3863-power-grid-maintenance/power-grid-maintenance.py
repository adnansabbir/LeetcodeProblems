class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        # create the graph
        graph = [[] for _ in range(c + 1)]
        online = [True] * (c+1)
        
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Create grids from the graph
        visited = set()
        grids = []
        conn_grid_map = [None] * (c+1)

        for node in range(1, c + 1):
            if node in visited:
                continue
            
            q = [node]
            grid_idx = len(grids)
            grids.append([])

            visited.add(node)
            while q:
                size = len(q)
                for _ in range(size):
                    curr_node = q.pop(0)
                    conn_grid_map[curr_node] = grid_idx
                    grids[grid_idx].append(curr_node)

                    for neighbour in graph[curr_node]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            grids[grid_idx].sort(reverse=True)
        
        result = []
        for command, station in queries:
            if command == 2:
                online[station] = False
            else:
                if online[station]:
                    result.append(station)
                    continue
                grid_idx = conn_grid_map[station]
                while grids[grid_idx] and not online[grids[grid_idx][-1]]:
                    grids[grid_idx].pop()

                if grids[grid_idx]:
                    result.append(grids[grid_idx][-1])
                else:
                    result.append(-1)
        return result
        