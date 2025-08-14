# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def getTreeWidth(root: Optional[TreeNode], pos = 0) -> List[int]:
            if not root:
                return [pos + 1, pos - 1]
            
            left_node = getTreeWidth(root.left, pos-1)
            right_node = getTreeWidth(root.right, pos+1)

            return [min(left_node[0], right_node[0]), max(left_node[1], right_node[1])]

        widthRange = getTreeWidth(root)
        offset = -widthRange[0]
        width = widthRange[1] - widthRange[0] + 1

        result = [[] for _ in range(width)]
        # print(widthRange, offset, width, result)

        q = [(root, offset)]
        while q:
            size = len(q)
            for _ in range(size):
                node, pos = q.pop(0)
                result[pos].append(node.val)
                
                if node.left:
                    q.append((node.left, pos-1))
                if node.right:
                    q.append((node.right, pos+1))

        return result