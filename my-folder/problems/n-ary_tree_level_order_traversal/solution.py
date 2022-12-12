"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                for c in x.children:
                    queue.append((c,level+1))
        print(sol)
        return sol
        