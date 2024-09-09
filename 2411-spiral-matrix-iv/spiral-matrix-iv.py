# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for j in range(n)] for i in range(m)]

        left, right, top, bottom = 0, n - 1, 0, m - 1
        pos = [0,0,'r']
        while head:
            result[pos[0]][pos[1]] = head.val
            if pos[2] == 'r':
                if pos[1] < right:
                    pos[1] += 1
                else:
                    pos[0] += 1
                    pos[2] = 'd'
                    top += 1
            elif pos[2] == 'd':
                if pos[0] < bottom:
                    pos[0] += 1
                else:
                    pos[1] -= 1
                    pos[2] = 'l'
                    right -= 1
            elif pos[2] == 'l':
                if pos[1] > left:
                    pos[1] -= 1
                else:
                    pos[0] -= 1
                    pos[2] = 'u'
                    bottom -= 1
            elif pos[2] == 'u':
                if pos[0] > top:
                    pos[0] -= 1
                else:
                    pos[1] += 1
                    pos[2] = 'r'
                    left += 1

            head = head.next

        return result