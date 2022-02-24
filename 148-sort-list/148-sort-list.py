# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitLinkedList(self, head: Optional[ListNode])-> Optional[ListNode]:
        
        fast = slow = prevSlow = head
        
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        
        prevSlow.next = None
        
        return [head, slow]
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        firstHalf, secondHalf = self.splitLinkedList(head)
        
        left = self.sortList(firstHalf)
        right = self.sortList(secondHalf)
        
        newHead = ListNode()
        
        if left.val<right.val:
            newHead.next = left
        else:
            newHead.next = right
            
        prevNode = newHead
        
        while left and right:
            if left.val < right.val:
                prevNode.next = left
                prevNode = left
                left = left.next
            else:
                prevNode.next = right
                prevNode = right
                right = right.next
        
        if left:
            prevNode.next = left
        elif right:
            prevNode.next = right
            
        return newHead.next
                
                    