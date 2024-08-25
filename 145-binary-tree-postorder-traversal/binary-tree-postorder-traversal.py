# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def post_order(node:Optional[TreeNode]):
            if not node:
                return
            

            post_order(node.left)
            post_order(node.right)

            result.append(node.val)
        
        post_order(root)
        return result
        