# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def traverse(node: TreeNode, depth: int):
            if not root:
                return
            
            if len(result) <= depth:
                result.append([])
            
            if depth%2 == 0:
                result[depth].append(node.val)
            else:
                result[depth].insert(0, node.val)
                
            if node.left:
                traverse(node.left, depth + 1)
            
            if node.right:
                traverse(node.right, depth + 1)
        
        traverse(root, 0)
        return result