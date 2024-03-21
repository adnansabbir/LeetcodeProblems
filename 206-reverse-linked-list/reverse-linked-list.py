# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # None<-1<-2<-3

        # prev    cur former  temp
        # 2       3   None       None

        prev = None
        curr = head
        former = head.next
        while curr and former:
            temp = former.next
            former.next = curr
            curr.next = prev
            
            prev = curr
            curr = former
            former = temp
        
        curr.next = prev
        return curr
        