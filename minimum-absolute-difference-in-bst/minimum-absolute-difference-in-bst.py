# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.result = 10**5
        self.prevVal = None
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            if self.prevVal is not None:
                self.result = min(self.result, abs(self.prevVal - root.val))
            
            self.prevVal = root.val
            inorder(root.right)
        
        inorder(root)
        return self.result
