# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        # l = []
        # def postorder(root):
        #     if root:
        #         postorder(root.left)
        #         postorder(root.right)
        #         l.append(root.val)
        # postorder(root)
        # return l
        
        #iterative using 2 stack
        # l = []
        # stack1 = deque()
        # stack2 = deque()
        # stack1.append(root)
        # while stack1:
        #     node = stack1.pop()
        #     if node:
        #         stack2.append(node)
        #         stack1.append(node.left)
        #         stack1.append(node.right)
        # while stack2:
        #     node = stack2.pop()
        #     l.append(node.val)
        # return l
        
        #iterative using 1 stack
        # stack = deque()
        # curr = root
        # l = []
        # while curr!=None or stack:
        #     if curr!=None:
        #         stack.append(curr)
        #         curr = curr.left
        #     else:
        #         temp = stack[-1].right
        #         if temp==None:
        #             temp = stack.pop()
        #             l.append(temp.val)
        #             while stack and temp == stack[-1].right:
        #                 temp = stack.pop()
        #                 l.append(temp.val)
        #         else:
        #             curr = temp
        # return l
        
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
        return postorder