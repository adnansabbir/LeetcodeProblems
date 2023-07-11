# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}

        # Creating the graph
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)

                if not curr.val in graph:
                    graph[curr.val] = []
                
                if curr.left:
                    if not curr.left.val in graph:
                        graph[curr.left.val] = []

                    graph[curr.val].append(curr.left.val)
                    graph[curr.left.val].append(curr.val)

                    queue.append(curr.left)
                
                if curr.right:
                    if not curr.right.val in graph:
                        graph[curr.right.val] = []

                    graph[curr.val].append(curr.right.val)
                    graph[curr.right.val].append(curr.val)

                    queue.append(curr.right)
        
        
        q2 = [target.val]
        result = []
        visited = set([target.val])
        while q2 and k >= 0:
            size = len(q2)
            for _ in range(size):
                curr = q2.pop(0)
                if k == 0:
                    result.append(curr)
                
                for neigh in graph[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q2.append(neigh)
            k -=1

        return result