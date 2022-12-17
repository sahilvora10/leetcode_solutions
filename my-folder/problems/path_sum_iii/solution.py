# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.totalcount = 0
        
        def hasPathSum(root,ts) -> bool:
            if not root:
                return None
            
            if root.val == ts:
                self.totalcount+=1
            hasPathSum(root.left,ts-root.val)
            hasPathSum(root.right,ts-root.val)
            
        def inorder(root):
            if not root:
                return
            # print(root.val)
            hasPathSum(root,targetSum)
            inorder(root.left)
            inorder(root.right)
                
        
        inorder(root)
        return self.totalcount
                
                
                
        
        
    
        