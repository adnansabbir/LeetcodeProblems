import sys

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n<2:
            return 0
        
        graph = {}
        for i, num in enumerate(arr):
            if num in graph:
                graph[num].append(i)
            else:
                graph[num] = [i]
        
        curr = [0]
        visited = {0}
        steps = 0
        
        while curr:
            nex = []
            
            for node in curr:
                if node == n-1:
                    return steps
            
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                graph[arr[node]].clear()

                for child in [node-1, node+1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)
            
            curr = nex
            steps+=1
        
        return -1
         
        
        