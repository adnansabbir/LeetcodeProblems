# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = head.next
        tHead = None
        
        a = head
        b = head.next
        
        while a and b:
            a.next = b.next
            b.next = a
            
            if tHead:
                tHead.next = b
            
            tHead = a
            a = a.next
            b = a.next if a else None
        
        return newHead