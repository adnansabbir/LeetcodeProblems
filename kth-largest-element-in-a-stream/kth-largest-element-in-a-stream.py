from queue import PriorityQueue

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.queue = PriorityQueue()
        self.k = k

        for num in nums:
            self.queue.put(num)
            if self.queue.qsize() > k:
                self.queue.get()
        

    def add(self, val: int) -> int:
        self.queue.put(val)
        if self.queue.qsize() > self.k:
            self.queue.get()
        return self.queue.queue[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)