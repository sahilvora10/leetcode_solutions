# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        hp = defaultdict(int)
        for i in range(n):
            hp[inorder[i]]=i
        # print(hp)
        
        def getTree(inorder_start,inorder_end,preorder_start,preorder_end):
            if preorder_start>preorder_end or inorder_start>inorder_end:
                return None
            x = preorder[preorder_start]
            root = TreeNode(x)
            xi = hp[x]
            nums_left = xi-inorder_start
            root.left = getTree(inorder_start,xi,preorder_start+1,preorder_start+nums_left)
            root.right = getTree(xi+1,inorder_end,preorder_start+nums_left+1,preorder_end)
            return root
        
        return getTree(0,n-1,0,n-1)