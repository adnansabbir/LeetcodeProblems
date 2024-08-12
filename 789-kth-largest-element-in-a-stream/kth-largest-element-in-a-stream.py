from bisect import bisect, insort

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_elems = sorted(nums)
        while len(self.k_elems) > self.k:
            self.k_elems.pop(0)
        

    def add(self, val: int) -> int:
        insort(self.k_elems, val)
        if len(self.k_elems) > self.k:
            self.k_elems.pop(0)
        return self.k_elems[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)