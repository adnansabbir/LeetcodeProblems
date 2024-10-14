from queue import PriorityQueue
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()

        for num in nums:
            q.put((-num, num))
        

        result = 0
        while k:
            num = q.get()[1]
            result += num
            q.put((-ceil(num/3), ceil(num/3)))
            k-=1

        return result
        