# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal = p.val if p.val <= q.val else q.val
        maxVal = p.val if p.val > q.val else q.val
        
        result = root
        
        while result:
            if minVal<= result.val <= maxVal:
                return result
            elif maxVal < result.val:
                result = result.left
            elif minVal > result.val:
                result = result.right
        return result
            
        