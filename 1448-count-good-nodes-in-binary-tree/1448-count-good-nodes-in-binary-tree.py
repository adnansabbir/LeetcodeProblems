class Solution:
    def goodNodes(self, root: TreeNode, maxParent = -10**5) -> int:
        if not root:
            return 0
        
        if root.val>=maxParent:
            maxParent = root.val
            return 1 + self.goodNodes(root.left, maxParent) + self.goodNodes(root.right, maxParent)
        return self.goodNodes(root.left, maxParent) + self.goodNodes(root.right, maxParent)
