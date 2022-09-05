"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        stack = [root]
        
        while stack:
            size = len(stack)
            result.append([n.val for n in stack])
            for _ in range(size):
                node = stack.pop(0)
                for child in node.children:
                    stack.append(child)
        
        return result