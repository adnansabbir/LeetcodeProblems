from queue import PriorityQueue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        pq = PriorityQueue()

        queue = [root]
        while queue:
            n = len(queue)

            total = 0
            for i in range(n):
                node = queue.pop(0)
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            pq.put(total)
            if pq.qsize() > k:
                pq.get()
        
        if pq.qsize() < k:
            return -1
        return pq.get()

        