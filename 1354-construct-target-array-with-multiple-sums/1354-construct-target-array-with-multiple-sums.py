from queue import PriorityQueue

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        q = PriorityQueue()
        for t in target:
            q.put(-t)
        total = sum(target)
        
        while q.queue[0] != -1:
            curr = -q.get()
            diff = total - curr
            
            if curr == 1 or diff == 1:
                return True
            
            if diff > curr or diff == 0 or curr % diff == 0:
                return False
            
            curr = curr%diff
            total = diff + curr
            q.put(-curr)
        
        return True
        
        