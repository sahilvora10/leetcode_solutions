"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l = []
        def post_n_array(root):
            if root:
                
                for c in root.children:
                    post_n_array(c)
                l.append(root.val)
        post_n_array(root)
        return l