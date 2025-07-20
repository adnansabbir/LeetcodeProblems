"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes_dict = {}

        def clone(parent):
            if not parent:
                return parent
            if parent not in nodes_dict:
                nodes_dict[parent.val] = Node(parent.val)
            
            for neighbor in parent.neighbors:
                if neighbor.val in nodes_dict:
                    cloned_neighbor = nodes_dict[neighbor.val]
                else:
                    cloned_neighbor = clone(neighbor)
                
                nodes_dict[parent.val].neighbors.append(cloned_neighbor)
                
            return nodes_dict[parent.val]
        
        return clone(node)
        