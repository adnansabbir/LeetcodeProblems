import heapq

class Point:
    @staticmethod
    def getDistance(co: List[int]):
        Xd = (co[0] - 0)**2
        Yd = (co[1] - 0)**2
        return Xd+Yd
    
    def __init__(self, val: List[int]):
        self.val = val
        self.distance = self.getDistance(self.val)
    
    def __repr__(self):
        return f"{self.val} -> {self.distance}"

    def __lt__(self, other: "Point"):
        return self.distance < other.distance

class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kPoints = heapq.nsmallest(k, [Point(p) for p in points])
        return [p.val for p in kPoints]
