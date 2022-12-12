"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        def pre_n_array(root):
            if root:
                # print('here')
                l.append(root.val)
                for c in root.children:
                    pre_n_array(c)
        pre_n_array(root)
        return l
        