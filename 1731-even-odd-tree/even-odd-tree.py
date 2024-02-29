# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]

        depth = 0
        while q:
            size = len(q)
            # print([v.val for v in q])
            if depth % 2 == 0:
                for i in range(size):
                    if q[i].val % 2 == 0:
                        # print(f"depth {depth}, idx {i} even")
                        return False
                    if i != 0 and q[i].val <= q[i-1].val:
                        # print(f"depth {depth}, idx {i} greater")
                        return False
            else:
                for i in range(size):
                    if not q[i].val % 2 == 0:
                        # print(f"depth {depth}, idx {i} odd")
                        return False
                    if i != 0 and q[i].val >= q[i-1].val:
                        # print(f"depth {depth}, idx {i} smaller")
                        return False

            for _ in range(size):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            depth += 1
        
        return True