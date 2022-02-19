from queue import PriorityQueue

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        q = PriorityQueue()
        for i, num in enumerate(nums):
            if num%2 != 0:
                nums[i] += num
            q.put(-nums[i])
        
        min_val = max(q.queue)
        max_val = q.get()
        
        result = abs(min_val-max_val)
        while max_val%2==0:
            q.put(max_val//2)
            min_val = max(min_val, max_val//2)
            max_val = q.get()
            result = min(result, abs(min_val-max_val))
    
        return result
        