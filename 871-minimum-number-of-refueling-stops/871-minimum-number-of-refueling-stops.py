import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        refills = [-startFuel]
        heapq.heapify(refills)
        
        tank = 0
        
        answer = 0
        for position, newFuel in stations:
            while refills and tank < position:
                tank += -heapq.heappop(refills)
                answer+=1
                
            if tank < position: return -1
            heapq.heappush(refills, -newFuel)
        
        return answer - 1