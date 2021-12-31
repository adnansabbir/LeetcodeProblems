# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMinMax(self, node, c_max, c_min):
        if node == None:
            return c_max - c_min
        
        c_max = max(c_max, node.val)
        c_min = min(c_min, node.val)
        
        return max(self.findMinMax(node.left, c_max, c_min), self.findMinMax(node.right, c_max, c_min))
    
    def maxAncestorDiff(self, root):
        if root == None:
            return 0
        
        return self.findMinMax(root, root.val, root.val)
        
        