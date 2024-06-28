from collections import defaultdict
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        roads_from_city = [0]*n
        
        for source, dest in roads:
            roads_from_city[source] += 1
            roads_from_city[dest] += 1

        roads_from_city.sort()
        
        result = 0
        for count, num in zip(roads_from_city, range(1, n+1)):
            result += count * num

        return result
        

        