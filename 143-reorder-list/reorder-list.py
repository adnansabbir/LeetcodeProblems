# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        q = []
        temp_head = head
        while temp_head:
            q.append(temp_head)
            temp_head = temp_head.next
        
        result = ListNode()
        temp_head = result
        is_start = True
        while q:
            temp_head.next = q.pop(0) if is_start else q.pop()
            is_start = not is_start
            temp_head = temp_head.next
        temp_head.next = None

        return result.next
        