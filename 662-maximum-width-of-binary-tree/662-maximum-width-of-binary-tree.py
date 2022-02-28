# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getWidth(self, root: Optional[TreeNode], depth: int, position: int, depthWidthMap: Dict[int, List[int]]):
        if not root:
            return 0
        
        if depth not in depthWidthMap:
            depthWidthMap[depth] = [position, position]
        else:
            depthWidthMap[depth][1] = position
        
        return max(
            abs(depthWidthMap[depth][0] - depthWidthMap[depth][1]),
            self.getWidth(root.left, depth+1, (2*position), depthWidthMap),
            self.getWidth(root.right, depth+1, (2*position)+1, depthWidthMap)
        )
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getWidth(root, 1, 1, {}) + 1
        