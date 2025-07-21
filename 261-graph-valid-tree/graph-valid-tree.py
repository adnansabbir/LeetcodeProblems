class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}

        # Creting the graph
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        queue = [(None, 0)]

        seen = set()
        processed = 0
        while queue:
            size = len(queue)

            for _ in range(size):
                parent, node = queue.pop(0)
                processed += 1
                if node in seen:
                    return False
                seen.add(node)

                queue +=[(node, neighbor) for neighbor in graph[node] if neighbor != parent]

        return processed == n
        
        