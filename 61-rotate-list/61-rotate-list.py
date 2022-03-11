# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode])-> int:
        count = 0
        while head:
            count+=1
            head = head.next
        
        return count
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.length(head)
        if not length:
            return head
        
        k = k%length
        
        if not k:
            return head
        
        newEnd = end = head
        endPos = 0
        
        while end and end.next:
            if endPos == k:
                newEnd = newEnd.next
            else:
                endPos +=1
                
            end = end.next
            
        end.next = head
        newHead = newEnd.next
        newEnd.next = None
        
        return newHead
        