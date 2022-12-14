# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        # l = []
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         l.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        # return l
        
        #iterative
        stack = deque()
        l = []
        node = root
        while True:
            if node!=None:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                l.append(node.val)
                node = node.right
        return l
        
        # preorder = []
        # inorder = []
        # postorder = []
        # stack = deque()
        # stack.append((root,1))
        # while stack:
        #     node,num = stack.pop()
        #     if node:
        #         if num==1:
        #             preorder.append(node.val)
        #             stack.append((node,num+1))
        #             if node.left:
        #                 stack.append((node.left,1))
        #         elif num==2:
        #             inorder.append(node.val)
        #             stack.append((node,num+1))
        #             if node.right:
        #                 stack.append((node.right,1))
        #         else:
        #             postorder.append(node.val)
        # print(preorder)
        # print(inorder)
        # print(postorder)
        # return inorder
        