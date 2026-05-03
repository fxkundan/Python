# Last updated: 04/05/2026, 00:33:22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result=[]
    def preorderHelp(self, root: Optional[TreeNode]):
            if(root):
                self.result.append(root.val)
                if(root.left):
                    ls = self.preorderHelp(root.left)
                    if(ls):
                        self.result.append()
                if(root.right):
                    rs = self.preorderHelp(root.right)
                    if(rs):
                        self.result.append(rs)
                    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.preorderHelp(root)
        return self.result