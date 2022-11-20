# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,inorder_arr):
        if node:
            
            self.inorder(node.left,inorder_arr)
            inorder_arr.append(node.val)
            self.inorder(node.right,inorder_arr)
    
    def getFloorAndCeil(self,arr, n, x):
        l = 0
        r = n-1
        floor = -1
        ceil = -1
        while l<=r:
            mid = (l+r)//2
            if x == arr[mid]:
                floor = arr[mid]
                ceil = arr[mid]
                break
            elif x>arr[mid]:
                floor = arr[mid]
                l = mid+1
            else:
                ceil = arr[mid]
                r = mid-1
        return [floor,ceil]
    
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        inorder_arr = []
        self.inorder(root,inorder_arr)
        # print(inorder_arr)
        ans = []
        for q in queries:
            ans.append(self.getFloorAndCeil(inorder_arr,len(inorder_arr),q))
        return ans
            