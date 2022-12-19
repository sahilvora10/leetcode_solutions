# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #brut force
        # def btpath(root,path,node):
        #     if not root:
        #         return False
        #     path.append(root)
        #     if root==node:
        #         return True
        #     if btpath(root.left,path,node) or btpath(root.right,path,node):
        #         return True
        #     path.pop()
        # p_path = []
        # btpath(root,p_path,p)
        # # print(p_path)
        # q_path = []
        # btpath(root,q_path,q)
        # # print(q_path)
        # i = 1
        # while i<len(p_path) and i<len(q_path):
        #     # print(p_path[i].val,q_path[i].val)
        #     if p_path[i]!=q_path[i]:
        #         # print('here')
        #         return p_path[i-1]
        #     i+=1
        # return p_path[i-1]
        if not root:
            return None
        if root==p:
            return p
        if root==q:
            return q
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        if not l:
            return r
        elif not r:
            return l
        else:
            return root
        