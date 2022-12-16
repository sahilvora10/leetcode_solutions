# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        sol = []
        queue.append(root)
        flag = True
        while queue:
            s = len(queue)
            l = [-1]*s
            for i in range(s):
                x = queue.popleft()
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                index = i if flag else s-1-i
                l[index] = (x.val)
            if l:
                sol.append(l)
            flag = not flag
        return sol
        