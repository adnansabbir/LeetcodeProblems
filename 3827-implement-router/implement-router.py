from sortedcontainers import SortedList

class Router:

    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.packetQ = deque()
        self.packets = {}
        self.count = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self._encode(source, destination, timestamp)
        if key in self.packets:
            return False

        if len(self.packetQ) == self.size:
            self.forwardPacket()

        self.packetQ.append(key)
        self.packets[key] = (source, destination, timestamp)

        if destination not in self.count:
            self.count[destination] = deque()
        
        self.count[destination].append(timestamp)
            
        return True

    def forwardPacket(self) -> List[int]:
        if not len(self.packets):
            return []
        key = self.packetQ.popleft()
        source, dest, time = self.packets[key]
        del self.packets[key]
        self.count[dest].popleft()
        return [source, dest, time]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.count.get(destination, [])
        if not timestamps:
            return 0
        
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        
        return right - left

    def _encode(self, source: int, destination: int, timestamp: int) -> int:
        # Encode uniquely into 1 number
        return (source << 40) | (destination << 20) | timestamp
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)