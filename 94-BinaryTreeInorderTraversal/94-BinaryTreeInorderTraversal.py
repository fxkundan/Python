# Last updated: 04/05/2026, 00:33:32
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
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
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.inOrderHelper(root)
        return self.result
                          
        