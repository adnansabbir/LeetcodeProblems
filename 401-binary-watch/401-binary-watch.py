class Solution: 
    def __init__(self):
        self.bit_map = defaultdict(list)
        for h in range(0, 12):
            for m in range(0, 60):
                bits = bin(h).count("1") + bin(m).count("1")
                self.bit_map[bits].append(f'{h}:{str(m).zfill(2)}')
                
        
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return self.bit_map[turnedOn]