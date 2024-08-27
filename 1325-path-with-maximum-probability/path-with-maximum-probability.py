class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        for i, [u,v] in enumerate(edges):
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]
        
        if start not in graph or end not in graph:
            return 0

        q = [(start, 1)]
        pFromStart = {start: 1}

        while q:
            size = len(q)
            for i in range(size):
                node, probability = q.pop(0)
                # print(node, graph[node].keys())
                for neighbour in graph[node].keys():
                    np = graph[node][neighbour] * probability
                    if neighbour not in pFromStart or pFromStart[neighbour] < np:
                        pFromStart[neighbour] = np
                        q.append((neighbour, np))
                    
        
        return pFromStart[end] if end in pFromStart else 0

