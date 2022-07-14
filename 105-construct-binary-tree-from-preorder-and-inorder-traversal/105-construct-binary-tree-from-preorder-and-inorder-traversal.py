# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = {}
        for i, num in enumerate(inorder):
            inorderMap[num] = i
        
        def build(iStart: int, iEnd: int):
            # print(preorder, inorder[iStart: iEnd], iStart, iEnd)
            if iEnd - iStart <= 0:
                return None
            if iEnd - iStart == 1:
                return TreeNode(preorder.pop(0))
        
        
            node = TreeNode(preorder.pop(0))
        
            node.left = build(iStart, inorderMap[node.val])
            node.right = build(inorderMap[node.val] + 1 , iEnd)
        
            return node
        
        return build(0, len(inorder))