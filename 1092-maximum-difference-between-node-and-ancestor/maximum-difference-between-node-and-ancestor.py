# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def getMaxDiff(node: Optional[TreeNode], low: int, high: int)-> int:
            if not node:
                return 0
            
            return max(
                max(abs(node.val - low), abs(node.val - high)),
                getMaxDiff(node.left, min(low, node.val), max(high, node.val)),
                getMaxDiff(node.right, min(low, node.val), max(high, node.val))
            )
        
        return getMaxDiff(root, root.val, root.val)