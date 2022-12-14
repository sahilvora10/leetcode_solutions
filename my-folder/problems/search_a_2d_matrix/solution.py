class Solution:
    def binary_search(self,l,r,nums,target):
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif target>nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ll = []
        # for i in matrix:
        #     for j in i:
        #         ll.append(j)
        # return self.binary_search(0,len(ll)-1,ll,target)
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = (m*n)-1
        while low<=high:
            mid = (low+high)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif target>matrix[mid//n][mid%n]:
                low = mid+1
            else:
                high = mid-1
        return False
        
        
                
        