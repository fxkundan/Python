# Last updated: 04/05/2026, 00:33:30
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
class Solution:
    def InOrderHelper(self,root: Optional[TreeNode],result):
        if(root):
            if(root.left):
                self.InOrderHelper(root.left,result)
            result.append(root.val)
            if(root.right):
                self.InOrderHelper(root.right,result)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        resultL=[]
        resultR=[]
        self.InOrderHelper(root.left,resultL)
        print(resultL)
        self.InOrderHelper(root.right,resultR)
        print(resultR)
        if(resultL  == list(reversed(resultR))):
            return True
        else:
            return False
   '''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)
        
    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        a = self.check(left.left, right.right)
        b = self.check(left.right, right.left)
        return a and b
        
        