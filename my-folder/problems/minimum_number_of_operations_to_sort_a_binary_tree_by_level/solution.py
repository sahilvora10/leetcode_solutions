# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minSwap(self,arr, n):
        ans = 0
        temp = arr.copy()
        h = {}
        temp.sort()
        for i in range(n):
            h[arr[i]] = i   
        init = 0
        for i in range(n):
            if (arr[i] != temp[i]):
                ans += 1
                init = arr[i]
                arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
                h[init] = h[temp[i]]
                h[temp[i]] = i
        return ans
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count = 0
        q = []
        q.append(root)
        while(len(q)>0):
            l = len(q)
            # print(l)
            layer = []
            while l!=0:
                n = q.pop(0)
                layer.append(n.val)
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
                l-=1
            c = self.minSwap(layer,len(layer)) if len(layer)>0 else 0
            # print(layer,c)
            count += c
        return count
            
            
        