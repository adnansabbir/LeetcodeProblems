# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = {}
        idx = 0
        for i, num in enumerate(inorder):
            inorderMap[num] = i
        
        def build(left: int, right: int):
            nonlocal idx
            if right - left <= 0:
                return None
            if right - left == 1:
                idx += 1
                return TreeNode(preorder[idx-1])
        
        
            idx += 1
            node = TreeNode(preorder[idx-1])
        
            node.left = build(left, inorderMap[node.val])
            node.right = build(inorderMap[node.val] + 1 , right)
        
            return node
        
        return build(0, len(inorder))