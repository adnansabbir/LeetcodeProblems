"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_clone_map = {None: None}
        
        curr = head
        while curr:
            original_clone_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            original_clone_map[curr].next = original_clone_map[curr.next]
            original_clone_map[curr].random = original_clone_map[curr.random]
            curr = curr.next
            
        return original_clone_map[head]
        
        