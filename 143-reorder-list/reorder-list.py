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
        if not head or not head.next or not head.next.next:
            return head

        def reverse_linked_list(head):
            if not head or not head.next:
                return head
            
            first, second = None, head

            while second:
                first, second.next, second = second, first, second.next
            return first

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_half = head
        second_half = reverse_linked_list(slow.next)
        slow.next = None
        
        temp = ListNode()
        while first_half or second_half:
            if first_half:
                temp.next = first_half
                temp = temp.next
                first_half = first_half.next
            if second_half:
                temp.next = second_half
                temp = temp.next
                second_half = second_half.next
        
        return head
            
                
        
        