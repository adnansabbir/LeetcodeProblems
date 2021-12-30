"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = [root]
        
        while len(queue):
            curr = queue.pop(0)
            Qrange = len(queue)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            
            for i in range(Qrange):
                curr.next = queue.pop(0)
                curr = curr.next
                
                if(curr.left):
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return root
            