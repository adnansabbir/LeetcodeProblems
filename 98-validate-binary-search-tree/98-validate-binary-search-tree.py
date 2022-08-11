import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low = -sys.maxsize, high = sys.maxsize) -> bool:
        if not root: return True
        
        if not low <= root.val <= high: return False
        
        return self.isValidBST(root.left, low, root.val-1) and self.isValidBST(root.right, root.val+1, high)