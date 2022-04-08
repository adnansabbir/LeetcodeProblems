from queue import PriorityQueue

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k

        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)