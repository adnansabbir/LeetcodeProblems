# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_map = defaultdict(int)
        
        newHead = tempHead = ListNode(0, head)
        
        while head:
            node_map[head.val]+=1
            head = head.next
        
        while tempHead and tempHead.next:
            if node_map[tempHead.next.val]>1:
                tempHead.next = tempHead.next.next
            else:
                tempHead = tempHead.next
        
        return newHead.next