# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = ListNode(0, head)
        fast = slow
        
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None
        
        return slow
        