# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        temp_result = result

        while head:
            if head.val == 0 and head.next:
                temp_result.next = head
                temp_result = temp_result.next
            else:
                temp_result.val += head.val
            
            head = head.next

        temp_result.next = None
        return result.next
        