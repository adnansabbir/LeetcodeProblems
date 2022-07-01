from queue import PriorityQueue

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        total = 0
        
        for i in range(len(boxTypes)):
            if truckSize == 0:
                return total
            elif truckSize >= boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                total += boxTypes[i][0]*boxTypes[i][1]
            else:
                total = total + (truckSize*boxTypes[i][1])
                truckSize = 0
        
        return total