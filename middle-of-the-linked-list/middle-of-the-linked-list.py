# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        fast_runner = head
        
        while fast_runner and fast_runner.next != None:
            runner = runner.next
            fast_runner = fast_runner.next.next
        
        return runner