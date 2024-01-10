# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {root.val : None}
        startNode = None

        stack = [root]
        # list down parents of each nodes
        while stack:
            curr = stack.pop(0)
            if curr.val == start:
                startNode = curr

            if curr.left:
                stack.append(curr.left)
                parents[curr.left.val] = curr
            if curr.right:
                stack.append(curr.right)
                parents[curr.right.val] = curr
        
        result = 0
        stack = [startNode]
        infectedNodeValues = set()
        taken = set([startNode.val])
        while stack:
            size = len(stack)
            for i in range(size):
                curr = stack.pop(0)
                if curr.val in infectedNodeValues:
                    continue
                
                infectedNodeValues.add(curr.val)
                if curr.left and curr.left.val not in taken:
                    stack.append(curr.left)
                    taken.add(curr.left.val)

                if curr.right and curr.right.val not in taken:
                    stack.append(curr.right)
                    taken.add(curr.right.val)

                if parents[curr.val] and parents[curr.val].val not in taken:
                    stack.append(parents[curr.val])
                    taken.add(parents[curr.val].val)  
            
            result += 1
        
        return result - 1
            
