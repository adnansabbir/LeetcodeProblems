class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}

        for i, m in enumerate(manager):
            if m == -1:
                continue
            
            if m not in graph:
                graph[m] = {'sub': [i]}
            else:
                graph[m]['sub'].append(i)
        
        def getTime(head)-> int:
            if head not in graph:
                return 0
            
            return informTime[head] + max(getTime(sub) for sub in graph[head]['sub'])

        return getTime(headID)
            
                