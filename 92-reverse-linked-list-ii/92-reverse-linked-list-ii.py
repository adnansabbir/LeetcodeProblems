# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        newHead = ListNode(None, head)
        preLeft = newHead
        postRight = newHead
        
        for _ in range(left-1):
            preLeft = preLeft.next
        
        for _ in range(right):
            postRight = postRight.next
        postRight = postRight.next
        
        prev = postRight
        curr = preLeft.next
        
        while left <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            left+=1
        
        preLeft.next = prev
        return newHead.next
        