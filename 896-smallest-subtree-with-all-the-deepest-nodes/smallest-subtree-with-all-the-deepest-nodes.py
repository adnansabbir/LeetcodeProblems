# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_node_map = {}

        def get_node_depth(node: Optional[TreeNode]):
            if not node:
                return [0,0]
            
            depth_node_map[node] = [
                max(get_node_depth(node.left)) + 1,
                max(get_node_depth(node.right)) + 1
            ]

            return depth_node_map[node]
        
        get_node_depth(root)
        # for key, val in depth_node_map.items():
        #     print(key.val, val)

        result = root
        while depth_node_map[result][0] != depth_node_map[result][1]:
            l, r = depth_node_map[result]
            if l > r:
                result = result.left
            else:
                result = result.right
        return result
            
            

        