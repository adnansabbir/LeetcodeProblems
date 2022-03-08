# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        
        while head and head.next:
            slow = slow.next
            head = head.next.next
            
            if slow == head:
                return True
        
        return False
        