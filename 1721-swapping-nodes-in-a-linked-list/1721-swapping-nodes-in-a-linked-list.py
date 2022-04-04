# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        
        while k>1:
            left = left.next
            k-=1
        
        tempLeft = left.next
        right = head
        while tempLeft:
            right = right.next
            tempLeft = tempLeft.next
        
        left.val, right.val = right.val, left.val
        return head