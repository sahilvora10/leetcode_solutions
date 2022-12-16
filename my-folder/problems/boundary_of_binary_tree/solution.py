# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        def isLeaf(root):
            if not root.left and not root.right:
                return True
            return False
        
        def addleaf(root):
            if isLeaf(root):
                sol.append(root.val)
                return 
            if root.left:
                addleaf(root.left)
            if root.right:
                addleaf(root.right)
                
        
        if not root:
            return []
        if not isLeaf(root):
            sol.append(root.val)
        curr = root.left
        while curr:
            if not isLeaf(curr):
                sol.append(curr.val)
            curr = curr.left if curr.left else curr.right
        addleaf(root)
        st = deque()
        curr = root.right
        while curr:
            if not isLeaf(curr):
                st.append(curr.val)
            curr = curr.right if curr.right else curr.left
        while st:
            sol.append(st.pop())
        return sol
            
        