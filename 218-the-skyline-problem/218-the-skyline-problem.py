class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # heap: take the highest, check if still in range, if not ignore and pop from heap
        # if curr building is in range -> push to heap
        def points():
            for l, r, h in buildings:
                yield l
                yield r
            
        pq = []
        j = 0
        ans = []
        for i in sorted(points()):
            while j < len(buildings) and buildings[j][0] <= i:
                heappush(pq, (-buildings[j][2], buildings[j][0], buildings[j][1]))
                j += 1
            while pq and pq[0][2] <= i:
                heappop(pq)
            height = -pq[0][0] if pq else 0
            if not ans or ans[-1][1] != height:
                ans.append((i, height))
        return ans