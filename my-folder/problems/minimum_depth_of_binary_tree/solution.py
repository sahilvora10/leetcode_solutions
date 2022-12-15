# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        l = 0
        while queue:
            l+=1
            s = len(queue)
            for i in range(s):
                x = queue.popleft()
                if x:
                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
                    if not x.left and not x.right:
                        return l
        return -1