# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        temp_head = head

        while temp_head:
            size += 1
            temp_head = temp_head.next

        result = []
        while head:
            result.append(head)
            temp_size = math.ceil(size/k)
            size -= temp_size
            k -= 1
            end_node = head
            while temp_size and head:
                end_node = head
                head = head.next
                temp_size -= 1
            end_node.next = None

        while k:
            result.append(None)
            k -= 1
        return result