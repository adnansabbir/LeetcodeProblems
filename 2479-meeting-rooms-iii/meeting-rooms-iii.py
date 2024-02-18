class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [[0,i] for i in range(n)]
        ans = [0]*n
        meetings.sort(key= lambda x: x[0])
        
        for curstart, curend in meetings:
            while rooms and rooms[0][0] < curstart:
                _, prevroom = heappop(rooms)
                heappush(rooms, [curstart, prevroom])
            prevend, prevroom = heappop(rooms)
            heappush(rooms, [prevend + (curend-curstart), prevroom])
            ans[prevroom] += 1
        return ans.index(max(ans))