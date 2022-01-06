class Solution:
    def getMinMaxDistance(self, trips: List[List[int]])-> List[int]:
        result = [trips[0][1], trips[0][2]]
        
        for trip in trips:
            if result[0]>trip[1]:
                result[0] = trip[1]
            if result[1]<trip[2]:
                result[1] = trip[2]
        
        return result
        
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_d, max_d = self.getMinMaxDistance(trips)
        
        onboards = [0]* (max_d + 1)
        total_onboard = 0
        
        for trip in trips:
            p, f, t = trip
            onboards[f]+=p
            onboards[t]-=p
            
        
        for passenger in onboards:
            total_onboard += passenger
            if total_onboard>capacity:
                return False
        
        return True
        
        