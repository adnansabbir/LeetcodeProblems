from queue import PriorityQueue

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        total = 0
        
        for boxes, units in boxTypes:
            if truckSize == 0:
                return total
            elif truckSize >= boxes:
                truckSize -= boxes
                total += boxes*units
            else:
                total = total + (truckSize*units)
                truckSize = 0
        
        return total