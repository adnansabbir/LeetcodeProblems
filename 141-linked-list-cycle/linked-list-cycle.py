# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        first, second = head, head.next

        while second and second.next:
            if first == second:
                return True
            first = first.next
            second = second.next.next
        return False
        