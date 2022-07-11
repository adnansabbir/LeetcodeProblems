# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def visit(node: Optional[TreeNode], depth: int):
            if not node:
                return
            if depth >= len(result):
                result.append(node.val)
            
            visit(node.right, depth+1)
            visit(node.left, depth+1)
        
        visit(root, 0)
        
        return result
            
        