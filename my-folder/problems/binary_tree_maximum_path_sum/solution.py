# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathsum(self,root,maxs):
        if not root:
            return 0
        l = max(0,self.pathsum(root.left,maxs))
        r = max(0,self.pathsum(root.right,maxs))
        maxs[0] = max(maxs[0],root.val+l+r)
        return root.val+max(l,r)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxs = [-1000000001]
        self.pathsum(root,maxs)
        return maxs[0]