# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        self.total = 0    
        
        def sum_to_root(root: Optional[TreeNode], parent: str):
            
            if not root.right and not root.left:
                self.total += int(f'{parent}{root.val}', 2)
                return
            
            if root.left:
                sum_to_root(root.left, f'{parent}{root.val}')
            
            if root.right:
                sum_to_root(root.right, f'{parent}{root.val}')
        
        sum_to_root(root, '')

        return self.total