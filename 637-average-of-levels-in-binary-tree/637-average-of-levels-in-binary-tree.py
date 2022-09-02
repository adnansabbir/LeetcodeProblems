# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = [root]
        result = []
        while queue:
            total = 0
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                total+= node.val
                
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            result.append(total/size)
        
        return result