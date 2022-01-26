# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root: TreeNode, value: int):
        if value <= root.val:
            if not root.left:
                root.left = TreeNode(value)
            else:
                self.insert(root.left, value)
        else:
            if not root.right:
                root.right = TreeNode(value)
            else:
                self.insert(root.right, value)
    
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        result = []
        
        def inorderTraversal(root: TreeNode, retVal = False):
            
            if not root:
                return
            
            if not retVal:
                inorderTraversal(root.left)
                self.insert(root1, root.val)
                inorderTraversal(root.right)
            else:
                inorderTraversal(root.left, retVal)
                result.append(root.val)
                inorderTraversal(root.right, retVal)
        
        if not root1:
            inorderTraversal(root2, True)
            return result 
        
        inorderTraversal(root2)
        inorderTraversal(root1, True)
        return result
        # print([r for r in inorderTraversal(root1, True)])