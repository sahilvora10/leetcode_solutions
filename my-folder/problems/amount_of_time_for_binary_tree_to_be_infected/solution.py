# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        hp = defaultdict(TreeNode)
        queue = deque()
        queue.append(root)
        targetNode = None
        while queue:
            x = queue.popleft()
            if x.val==start:
                targetNode = x
            if x.left:
                queue.append(x.left)
                hp[x.left] = x
            if x.right:
                queue.append(x.right)
                hp[x.right] = x
        # print(targetNode)
        visited = {}
        queue = deque()
        queue.append(targetNode)
        minute = -1
        while queue:
            s = len(queue)
            for i in range(s):
                x = queue.popleft()
                visited[x] = 1
                if x.left and x.left not in visited:
                    queue.append(x.left)
                if x.right and x.right not in visited:
                    queue.append(x.right)
                if x in hp and hp[x] not in visited:
                    queue.append(hp[x])
            minute+=1
        return minute
                