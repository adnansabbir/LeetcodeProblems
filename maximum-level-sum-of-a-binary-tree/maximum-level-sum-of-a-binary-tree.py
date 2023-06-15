# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        currSumLevel = [0, 1]
        maxSumLevel = [-10**6, 1]

        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                currSumLevel[0] += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            if currSumLevel[0] > maxSumLevel[0]:
                maxSumLevel = currSumLevel.copy()
            
            currSumLevel[0] = 0
            currSumLevel[1] += 1

        return  maxSumLevel[1]