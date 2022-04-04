# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, temp = 0, head
        
        while temp:
            n+=1
            temp = temp.next
            
        if k > n//2:
            k = n - k + 1
        
        LP = RP = None
        
        temp = ListNode(0, head)
        for i in range(k):
            LP = temp
            temp = temp.next
            
        temp = ListNode(0, head)
        for i in range(n-k+1):
            RP = temp
            temp = temp.next
        
        if LP == RP:
            return head
        
        Left = LP.next
        Right = RP.next
        LP.next, RP.next = RP.next, LP.next
        Left.next, Right.next = Right.next, Left.next 
        
        return head if k > 1 else Right 