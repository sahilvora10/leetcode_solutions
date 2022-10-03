class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minv = 5001
        while l<=r:
            
            if nums[l]<nums[r]:
                minv = min(minv,nums[l])
                return minv
            mid = (l+r)//2
            if nums[l]<=nums[mid]:
                minv = min(minv,nums[l])
                l = mid+1
            else:
                minv = min(minv,nums[mid])
                r = mid-1
        return minv
            
        
        