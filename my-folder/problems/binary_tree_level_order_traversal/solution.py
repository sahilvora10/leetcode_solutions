# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        sol = []
        queue.append((root,0))
        while queue:
            x,level = queue.popleft()
            if x:
                if level<len(sol):
                    sol[level].append(x.val)
                else:
                    sol.append([x.val])
                if x.left:
                    queue.append((x.left,level+1))
                if x.right:
                    queue.append((x.right,level+1)) 
        print(sol)
        return sol
        