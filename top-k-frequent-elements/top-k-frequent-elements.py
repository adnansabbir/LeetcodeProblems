import heapq

class Node(object):
    def __init__(self, val: int, freq: int):
        self.val = val
        self.freq = -freq
    
    def __repr__(self):
        return f'{self.val}-{self.freq}'
    
    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.defaultdict(int)
        uniqNums = set()
        
        for num in nums:
            frequency[num]+=1
            uniqNums.add(num)
        
        heapedNumNodes = [Node(num, frequency[num]) for num in uniqNums]
        heapq.heapify(heapedNumNodes)
        
        result = []
        while k:
            result.append(heapq.heappop(heapedNumNodes).val)
            k -=1
        
        return result