# Last updated: 04/05/2026, 00:33:21
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result=[]
    def postorderHelp(self, root: Optional[TreeNode]):
        if(root):
            if(root.left):
                ls = self.postorderHelp(root.left)
                if(ls):
                    self.result.append()
            if(root.right):
                rs=self.postorderHelp(root.right)
                if(rs):
                    self.result.append()
            self.result.append(root.val)
            
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.postorderHelp(root)
        return self.result
        
        