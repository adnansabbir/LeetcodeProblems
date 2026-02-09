# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        nodes = []

        def collect_nodes(node: Optional[TreeNode]):
            if not node:
                return
            
            collect_nodes(node.left)
            nodes.append(node)
            collect_nodes(node.right)
        
        def build_tree(boundry: tuple) -> Optional[TreeNode]:
            if boundry[0] > boundry[1]:
                return None
            idx = sum(boundry) // 2
            nodes[idx].left = build_tree((boundry[0], idx - 1))
            nodes[idx].right = build_tree((idx + 1, boundry[1]))
            return nodes[idx]
        
        collect_nodes(root)
        return build_tree((0, len(nodes) - 1))
        