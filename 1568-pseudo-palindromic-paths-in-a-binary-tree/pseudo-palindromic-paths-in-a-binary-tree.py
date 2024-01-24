# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPseudoPalindrome(freq):
            return sum([0 if f % 2 == 0 else 1 for f in freq]) < 2

        def getPalindromeCount(root: Optional[TreeNode], freq = [0 for i in range(10)])-> int:
            if not root:
                return 0

            freq[root.val] += 1

            if not root.left and not root.right:
                if isPseudoPalindrome(freq):
                    result = 1
                else:
                    result = 0
            else:
                result = getPalindromeCount(root.left, freq) + getPalindromeCount(root.right, freq)
            freq[root.val] -= 1
            return result

        return getPalindromeCount(root)