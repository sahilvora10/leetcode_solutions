# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode],maxd) -> int:
        if root is None:
            return 0
        
        lh = self.maxDepth(root.left,maxd)
        rh = self.maxDepth(root.right,maxd)
        maxd[0] = max(maxd[0],lh+rh)
        # print(root.val,maxd[0])
        return 1+max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd=[0]
        self.maxDepth(root,maxd)
        print(maxd[0])
        return maxd[0]