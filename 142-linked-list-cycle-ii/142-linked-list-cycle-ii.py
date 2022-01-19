# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique = set()
        
        temp = head
        
        while temp:
            unique.add(temp)
            if temp.next in unique:
                return temp.next
            
            temp = temp.next
        
        return None
        