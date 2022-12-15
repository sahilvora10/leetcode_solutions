# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def dfs(self,root):
        if not root:
            return
        if root:
            print(root.val)
            self.dfs(root.left)
            self.dfs(root.right)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def hasPathSum(root,targetSum,path) -> bool:
            if not root:
                return None
            
            targetSum-=root.val
            path.append(root.val)
            if not root.left and not root.right and targetSum==0:
                ans.append(path.copy())
            else:
                hasPathSum(root.left,targetSum,path)
                hasPathSum(root.right,targetSum,path)
            path.pop()
        ans = []
        hasPathSum(root,targetSum,[])
        return ans