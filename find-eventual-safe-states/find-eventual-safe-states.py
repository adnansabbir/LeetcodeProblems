# dp = {0: false, 1: false, 2: true, 5: true, 3: false, 4: true}
# visited = {4}

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dp = {}

        def collectSafeNodes(root, visited = set())-> bool:
            if root in dp:
                return dp[root]
            
            dp[root] = True
            if graph[root]:
                for neighbour in graph[root]:
                    if neighbour in visited:
                        dp[root] = False
                        return False
                    visited.add(neighbour)
                    dp[root] = dp[root] and collectSafeNodes(neighbour, visited)
                    visited.remove(neighbour)

            return dp[root]

        result = []
        for i in range(len(graph)):
            if i not in dp:
                collectSafeNodes(i, set([i]))
            if dp[i]:
                result.append(i)

        return result