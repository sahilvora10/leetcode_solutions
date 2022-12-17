# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        hp = defaultdict(TreeNode)
        queue = deque()
        queue.append(root)
        targetNode = None
        while queue:
            x = queue.popleft()
            if x==target:
                targetNode = x
            if x.left:
                queue.append(x.left)
                hp[x.left] = x
            if x.right:
                queue.append(x.right)
                hp[x.right] = x
        # print(hp)
        # print(targetNode)
        # print(hp[targetNode])
        queue = deque()
        visited = {}
        sol = []
        queue.append((targetNode,0))
        while queue:
            x,dist = queue.popleft()
            visited[x] = 1
            if dist==k:
                sol.append(x.val)
            if x in hp and hp[x] not in visited:
                queue.append((hp[x],dist+1))
            if x.left and x.left not in visited:
                queue.append((x.left,dist+1))
            if x.right and x.right not in visited:
                queue.append((x.right,dist+1))
            
        return sol
                
        
        