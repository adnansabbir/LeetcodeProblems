# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node: TreeNode, arr: List[int]) -> List[int]:
            if node:
                if not node.left and not node.right:
                    arr.append(node.val)
                
                dfs(node.left, arr)
                dfs(node.right, arr)
            return arr
        return dfs(root1, []) == dfs(root2, [])