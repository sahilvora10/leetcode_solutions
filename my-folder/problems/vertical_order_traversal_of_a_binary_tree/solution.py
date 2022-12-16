# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def inorder(self,root,vertical,level,hp):
        if not root:
            return
        self.inorder(root.left,vertical-1,level+1,hp)
        hp[vertical].append((level,root.val))
        self.inorder(root.right,vertical+1,level+1,hp)
            
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #node,xaxis(vertical),yaxis(level)
        #dict {vertical line ie xaxis : [(level,val),(level,val)...]}
        queue = deque()
        hp = defaultdict(list)
        # queue.append((root,(0,0)))
        # while queue:
        #     x,(i,j) = queue.popleft()
        #     if x:
        #         if x.left:
        #             queue.append((x.left,(i-1,j+1)))
        #         if x.right:
        #             queue.append((x.right,(i+1,j+1)))
        #     hp[i].append((j,x.val))
        self.inorder(root,0,0,hp)
        print(hp)
        sol = []
        for i in sorted(hp.keys()):
            l = []
            for j in sorted(hp[i]):
                l.append(j[1])
            sol.append(l)
        return sol
        
            
        