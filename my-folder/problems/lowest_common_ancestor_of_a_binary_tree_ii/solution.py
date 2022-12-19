# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def LCA(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if not root:
            return None
        
        l = self.LCA(root.left,p,q)
        r = self.LCA(root.right,p,q)
        if root==p:
            self.pflag = True
            return p
        if root==q:
            self.qflag = True
            return q
        if not l:
            return r
        elif not r:
            return l
        else:
            return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pflag = False
        self.qflag = False
        a = self.LCA(root,p,q)
        print(self.pflag)
        print(self.qflag)
        if self.pflag and self.qflag:
            return a
        return None