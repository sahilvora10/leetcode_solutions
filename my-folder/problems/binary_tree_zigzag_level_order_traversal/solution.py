# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        sol = []
        queue.append(root)
        flag = True
        while queue:
            s = len(queue)
            l = []
            for i in range(s):
                x = queue.popleft()
                if x:
                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
                    l.append(x.val)
            if l:
                if flag:
                    sol.append(l)
                else:
                    sol.append(l[::-1])
                flag = not flag
        return sol
        