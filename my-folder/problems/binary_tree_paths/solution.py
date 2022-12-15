# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def btpath(root,path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                ans.append(path.copy())
            btpath(root.left,path)
            btpath(root.right,path)
            path.pop()
        ans = []
        btpath(root,[])
        for j in range(len(ans)):
            a = ans[j]
            s = ""
            for i in range(len(a)-1):
                s +=str(a[i])
                s+='->'
            s+=str(a[len(a)-1])
            ans[j] = s
        return ans
            