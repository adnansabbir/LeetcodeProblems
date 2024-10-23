# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = [root]

        while queue:
            size = len(queue)

            sum_by_node = []
            total = 0
            for _ in range(size):
                curr_node = queue.pop(0)
                sum_by_node.append([curr_node, 0])

                if curr_node.left:
                    sum_by_node[-1][1] += curr_node.left.val
                    total += curr_node.left.val
                    queue.append(curr_node.left)

                if curr_node.right:
                    sum_by_node[-1][1] += curr_node.right.val
                    total += curr_node.right.val
                    queue.append(curr_node.right)
            
            for node, node_sum in sum_by_node:
                if node.left:
                    node.left.val = total - node_sum
                if node.right:
                    node.right.val = total - node_sum
            
        root.val = 0

        return root
        