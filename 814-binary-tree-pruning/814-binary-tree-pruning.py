# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def trim(root:Optional[TreeNode])-> int:
            if not root: return 0
            
            left = trim(root.left)
            right = trim(root.right)
            
            if not left:
                root.left = None
            
            if not right:
                root.right = None
                
            return min(root.val + left + right, 1)
        
        if not trim(root):
            return None
        return root