# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_critical_point_idx = None
        last_critical_point_idx = None

        idx = 0
        prev_node = head
        curr_node = head.next
        min_distance = -1
        max_distance = -1

        while curr_node and curr_node.next:
            if (prev_node.val > curr_node.val < curr_node.next.val) or (prev_node.val < curr_node.val > curr_node.next.val):
                if first_critical_point_idx == None:
                    first_critical_point_idx = idx
                else:
                    max_distance = idx - first_critical_point_idx
                    if min_distance == -1:
                        min_distance = idx - last_critical_point_idx
                    else:
                        min_distance = min(min_distance, idx - last_critical_point_idx)
                last_critical_point_idx = idx
            
            prev_node = curr_node
            curr_node = curr_node.next
            idx += 1

        return [min_distance, max_distance]