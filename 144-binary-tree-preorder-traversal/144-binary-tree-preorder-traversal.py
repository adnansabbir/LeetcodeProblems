# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode], result = None) -> List[int]:
        if result == None:
            result = []
        
        if not root:
            return []
        
        result.append(root.val)
        self.preorderTraversal(root.left, result)
        self.preorderTraversal(root.right, result)
        
        return result
        