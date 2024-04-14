# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    
    def addLeftLeaf(self, root: Optional[TreeNode], pos: str):
        if not root:
            return
        
        if pos == 'L' and not root.left and not root.right:
            self.total+=root.val
        
        self.addLeftLeaf(root.left, 'L')
        self.addLeftLeaf(root.right, 'R')
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.addLeftLeaf(root.left, 'L')
        self.addLeftLeaf(root.right, 'R')
        
        return self.total