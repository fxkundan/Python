# Last updated: 04/05/2026, 00:33:10
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        result = []
        def inOrderHelper(self, root: Optional[TreeNode]):
            # print(self.result)
            if(root):
                if(root.left):
                    ls = self.inOrderHelper(root.left)
                    if(ls):
                        self.result.append()
                self.result.append(root.val)
                if(root.right):
                    rs = self.inOrderHelper(root.right)
                    if(rs):
                        self.result.append(rs)
                        
        def FindKth(self,x):
            return self.result[x];
           
                    
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            self.result = []
            self.inOrderHelper(root)
            print(self.result)
            return self.FindKth(k-1)
        