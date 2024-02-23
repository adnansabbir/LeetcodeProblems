class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}

        for DA, DB, price in flights:
            if not DA in graph:
                graph[DA] = []
            
            graph[DA].append((DB, price))
        
        result = -1

        bfs = [(src, 0)]
        minCostToCity = {src: 0}
        for i in range(k + 2):
            if not len(bfs):
                return result
            size = len(bfs)
            for _ in range(size):
                currCity, cost = bfs.pop(0)
                if currCity == dst:
                    result = cost if result == -1 else min(result, cost)
                elif currCity in graph:
                    for dstCity, dstPrice in graph[currCity]:
                        if dstCity not in minCostToCity or minCostToCity[dstCity] > cost + dstPrice:
                            bfs.append((dstCity, cost + dstPrice))
                            minCostToCity[dstCity] = cost + dstPrice


        return result
        