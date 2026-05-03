# Last updated: 04/05/2026, 00:33:29
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root):
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        else:
            return 0