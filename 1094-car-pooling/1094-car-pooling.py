class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_dis = max([t[2] for t in trips]) + 1
        
        quantity = [0]*max_dis
        
        for trip in trips:
            p, f, t = trip
            
            for i in range(f, t):
                quantity[i] += p
                
                if quantity[i] > capacity:
                    return False
        
        return True
        
        