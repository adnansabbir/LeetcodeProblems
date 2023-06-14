# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode], minMax = [None, None]) -> int:
        # print(root.val if root else None, minMax)
        if not root:
            return 10**5
        left = self.getMinimumDifference(root.left, [minMax[0], root.val])
        right = self.getMinimumDifference(root.right, [root.val, minMax[1]])

        currDiff = 10**5
        if minMax[0] != None:
            currDiff = min(currDiff, root.val - minMax[0])
        if minMax[1] != None:
            currDiff = min(currDiff, minMax[1] - root.val)
        
        result = min(currDiff, left, right)
        # print(f'{root.val} returning {result}')
        return result
