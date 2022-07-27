# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode], child: Optional[TreeNode] = None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return child
        
        if root.right:
            root.right = self.flatten(root.right, child)
        elif child:
            root.right = child
        
        self.flatten(root.left, root.right)
        
        if root.left:
            root.right = root.left
            root.left = None
        
        return root
        
        