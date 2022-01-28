# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], result = None) -> List[int]:
        if result==None:
            result = []
        
        if not root:
            return []
        
        self.inorderTraversal(root.left, result)
        result.append(root.val)
        self.inorderTraversal(root.right, result)
        
        return result
        