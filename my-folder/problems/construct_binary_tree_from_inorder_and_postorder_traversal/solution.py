# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        hp = defaultdict(int)
        for i in range(n):
            hp[inorder[i]]=i
        # print(hp)
        
        def getTree(inorder_start,inorder_end,postorder_start,postorder_end):
            if postorder_start>postorder_end or inorder_start>inorder_end:
                return None
            x = postorder[postorder_end]
            root = TreeNode(x)
            xi = hp[x]
            nums_left = xi-inorder_start
            root.left = getTree(inorder_start,xi,postorder_start,postorder_start+nums_left-1)
            root.right = getTree(xi+1,inorder_end,postorder_start+nums_left,postorder_end-1)
            return root
        
        return getTree(0,n-1,0,n-1)
        