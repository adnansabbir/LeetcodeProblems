# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        def getLeftMaxDistance(node: TreeNode, index = 0, start = True)-> int:
            if not node: return index
            result = min(
                getLeftMaxDistance(node.left, index - 1, False),
                getLeftMaxDistance(node.right, index + 1, False)
            )
            return -(result + 1) if start else result
        
        def getRightMaxDistance(node: TreeNode, index = 0, start = True)-> int:
            if not node: return index
            result = max(
                getRightMaxDistance(node.left, index - 1, False),
                getRightMaxDistance(node.right, index + 1, False)
            )
            return (result - 1) if start else result
        
        leftDistance = getLeftMaxDistance(root)
        rightDistance = getRightMaxDistance(root)
        result = [[] for _ in range(leftDistance + rightDistance + 1)]
        
        def insertInVerticalOrder(node:TreeNode, index:int, depth=0):
            if not node: return
            result[index].append((depth, node.val))
            depth+=1
            insertInVerticalOrder(node.left, index-1, depth)
            insertInVerticalOrder(node.right, index+1, depth)
        
        insertInVerticalOrder(root, leftDistance)
        for i, res in enumerate(result):
            # print('Original', res, result)
            res.sort()
            result[i] = [val[1] for val in res]
            # print('Sorted', res, result)
        
        return result