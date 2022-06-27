# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        reverse = False
        while queue:
            size = len(queue)
            tempResult = []
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tempResult.append(node.val)
            
            if reverse:
                tempResult.reverse()
            reverse = not reverse
            result.append(tempResult)
            tempResult = []
        
        return result