# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getRootsToLeafPath(self, root: Optional[TreeNode], result: List[str], parent: str)-> List[str]:
        if root == None:
            return
        
        currPath = f'{parent}->{root.val}' if parent else f'{root.val}'
        
        if not root.left and not root.right:
            result.append(currPath)
            
        self.getRootsToLeafPath(root.left, result, currPath)
        self.getRootsToLeafPath(root.right, result, currPath)
        
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.getRootsToLeafPath(root, result, '')
        return result