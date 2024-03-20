# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prePointA = ListNode(0, list1)
        preResult = prePointA

        for _ in range(a):
            prePointA = prePointA.next
        
        prePointB = prePointA
        for _ in range(b - a + 1):
            prePointB = prePointB.next

        prePointA.next = list2

        while list2.next:
            list2 = list2.next
        
        list2.next = prePointB.next
        
        return preResult.next