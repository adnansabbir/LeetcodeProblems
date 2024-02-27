# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode, is_root=True) -> int:
        if not root:
            return 0

        if is_root:
            self.diameter = 0

        left_length = 0
        right_length = 0

        if root.left:
            left_length = self.diameterOfBinaryTree(root.left, False) + 1

        if root.right:
            right_length = self.diameterOfBinaryTree(root.right, False) + 1

        if left_length + right_length > self.diameter:
            self.diameter = left_length + right_length

        if is_root:
            return self.diameter

        return max(left_length, right_length)
        