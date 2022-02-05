from queue import PriorityQueue

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        mergedList = pointer = ListNode(0)
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put(PrioritizedItem(l.val, l))
        
        
        while not q.empty():
            node = q.get().item
            pointer.next = ListNode(node.val)
            pointer = pointer.next
            
            node = node.next
            if node:
                q.put(PrioritizedItem(node.val, node))
        
        return mergedList.next
        
        
        