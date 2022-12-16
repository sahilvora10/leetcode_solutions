# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        sol = []
        queue.append(root)
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
                sol.append(l[-1])
        return sol
        