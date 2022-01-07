import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.node = []
        temp = head
        while temp != None:
            self.node.append(temp)
            temp = temp.next
        

    def getRandom(self) -> int:
        return self.node[random.randint(0, len(self.node)-1)].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()