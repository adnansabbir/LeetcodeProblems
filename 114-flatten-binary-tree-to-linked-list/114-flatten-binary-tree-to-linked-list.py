# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        nodes = []
        
        def traverse(root: Optional[TreeNode]):
            if not root:
                return
            
            nodes.append(root)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        
        for i, node in enumerate(nodes[1:]):
            nodes[i].left = None
            nodes[i].right = node
        