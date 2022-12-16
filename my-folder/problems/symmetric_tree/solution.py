# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def symm(l,r):
            if not l and not r:
                return True
            if (not l and r) or (not r and l):
                return False
            return l.val == r.val and symm(l.left,r.right) and symm(l.right,r.left)
        
        return symm(root.left,root.right)