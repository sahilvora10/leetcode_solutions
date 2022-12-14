# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        # l = []
        # def preorder(root):
        #     if root:
        #         l.append(root.val)
        #         preorder(root.left)
        #         preorder(root.right)
        # preorder(root)
        # return l
        
        #iterative
        # l = []
        # stack = deque()
        # stack.append(root)
        # while stack:
        #     rt = stack.pop()
        #     if rt:
        #         l.append(rt.val)
        #         stack.append(rt.right)
        #         stack.append(rt.left)
        # return l
        
        # #all together
        preorder = []
        inorder = []
        postorder = []
        stack = deque()
        stack.append((root,1))
        while stack:
            node,num = stack.pop()
            if node:
                if num==1:
                    preorder.append(node.val)
                    stack.append((node,num+1))
                    if node.left:
                        stack.append((node.left,1))
                elif num==2:
                    inorder.append(node.val)
                    stack.append((node,num+1))
                    if node.right:
                        stack.append((node.right,1))
                else:
                    postorder.append(node.val)
        print(preorder)
        print(inorder)
        print(postorder)
        return preorder