from functools import lru_cache

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def getMin(wIdx = 0, assignedBikes = '0'*len(bikes)) -> int:
            if wIdx == len(workers):
                return 0
            
            min_distance = None
            for i in range(len(bikes)):
                if assignedBikes[i] == '1':
                    continue
                
                wx, wy, bx, by = workers[wIdx] +  bikes[i]
                distance = abs(wx-bx) + abs(wy-by)

                assignedBikes = assignedBikes[:i] + '1' + assignedBikes[i+1:]
                rest_distance = getMin(wIdx + 1, assignedBikes)

                if min_distance == None:
                    min_distance = distance + rest_distance
                else:
                    min_distance = min(min_distance, distance + rest_distance)
                
                assignedBikes = assignedBikes[:i] + '0' + assignedBikes[i+1:]
            return min_distance
        
        return getMin()
        