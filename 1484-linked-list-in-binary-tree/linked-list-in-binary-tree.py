# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, listNode, treeNode):
        if not listNode:
            return True
        if not treeNode or treeNode.val != listNode.val:
            return False

        return (
            self.helper(listNode.next, treeNode.left) or 
            self.helper(listNode.next, treeNode.right)
        )

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.helper(head, root):
            return True
        
        if not root:
            return False
        return (
            self.isSubPath(head, root.left) or 
            self.isSubPath(head, root.right)
        )
            

        