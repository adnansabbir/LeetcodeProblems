# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        preRight = ListNode(None, head)
        right = preRight
        newHead = ListNode(None)
        left = newHead
        
        while right and right.next:
            if right.next.val < x:
                left.next = right.next
                left = left.next
                right.next = right.next.next
            else:
                right = right.next
        
        left.next = preRight.next
        return newHead.next