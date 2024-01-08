# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        stack = [root]

        while stack:
            currNode = stack.pop(0)
            if currNode.val >= low and currNode.val <= high:
                result += currNode.val
            
            if currNode.left:
                stack.append(currNode.left)

            if currNode.right:
                stack.append(currNode.right)

        return result
        