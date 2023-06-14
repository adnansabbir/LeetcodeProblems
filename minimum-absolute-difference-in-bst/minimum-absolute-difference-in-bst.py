# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodeValues = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodeValues.append(root.val)
            dfs(root.right)
        
        dfs(root)
        result = min([v - nodeValues[i] for i, v in enumerate(nodeValues[1:])])
        # print(f'{root.val} returning {result}')
        return result
