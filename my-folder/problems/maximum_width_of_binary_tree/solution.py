# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        # sol = []
        queue.append((root,0))
        maxw = -1
        while queue:
            s = len(queue)
            l = []
            minid = queue[0][1]
            for i in range(s):
                x,ind = queue.popleft()
                if x:
                    if x.left:
                        queue.append((x.left,(2*(ind-minid))+1))
                    if x.right:
                        queue.append((x.right,(2*(ind-minid))+2))
                    l.append((x.val,ind))
            maxw = max(maxw,l[-1][1]-l[0][1]+1)
            # sol.append(l)
                
        # print(sol)
        return maxw
        