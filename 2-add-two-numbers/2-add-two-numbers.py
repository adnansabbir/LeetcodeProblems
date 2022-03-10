# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbersRecursion(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        if not l1 and not l2 and not carry:
            return None
        elif not l1 and not l2 and carry:
            return ListNode(carry)
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        summation = val1+val2+carry
        
        newNode = ListNode(summation%10)
        nextNode = self.addTwoNumbersRecursion(l1.next if l1 else None, l2.next if l2 else None, 1 if summation>9 else 0)
        newNode.next = nextNode
        
        return newNode
        
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwoNumbersRecursion(l1, l2, 0)
        