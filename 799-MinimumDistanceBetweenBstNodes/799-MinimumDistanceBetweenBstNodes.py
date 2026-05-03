# Last updated: 04/05/2026, 00:32:48
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        result=[]
        def inOrderHelper(self, root: Optional[TreeNode]):
        #if no node
            print(self.result)
            if(root):
                # for left subtree
                if(root.left):
                    ls = self.inOrderHelper(root.left)
                    if(ls):
                        self.result.append()
                #for root node
                self.result.append(root.val)
                #for right subtree
                if(root.right):
                    rs = self.inOrderHelper(root.right)
                    if(rs):
                        self.result.append(rs)
        def FindMin(self):
            dif = float('inf')
            for i in range(1,len(self.result)):
                if dif > (self.result[i] - self.result[i-1]):
                    dif = (self.result[i] - self.result[i-1])
            return dif
        def minDiffInBST(self, root: Optional[TreeNode]) -> int:
            self.result = []
            self.inOrderHelper(root)
            return self.FindMin()
            