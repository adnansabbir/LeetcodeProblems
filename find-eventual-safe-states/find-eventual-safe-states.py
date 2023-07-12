class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dp = {}

        # We are using dfs to go traverse
        # we are keeping track of visited noted with the visited variable
        def dfs(root, visited)-> bool:
            # If the result is already there return it
            if root in dp:
                return dp[root]
            
            # Initially we are assuming the current node is safe
            dp[root] = True

            # if there is neighbours we will iterate them and decide if current node is safe
            # else we can say this is a safe node
            if graph[root]:
                for neighbour in graph[root]:
                    # If node is already visited than it's a cycle
                    if neighbour in visited:
                        dp[root] = False
                        return dp[root]

                    # If any neighbour is not safe current node will be marked unsafe    
                    visited.add(neighbour)
                    dp[root] = dp[root] and dfs(neighbour, visited)
                    visited.remove(neighbour)

                    # If current node is already marked unsafe we don't need to check the rest of the neighbours
                    if not dp[root]:
                        break

            return dp[root]

        result = []
        visited = set()
        for i in range(len(graph)):
            if i not in dp:
                visited.add(i)
                dfs(i, visited)
                visited.remove(i)
            
            # Since we need to return result sorted in ascending order, 
            # and we are iterating in ascending order whenever we find a safe node we store it
            if dp[i]:
                result.append(i)

        return result