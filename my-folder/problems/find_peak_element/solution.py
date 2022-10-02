class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binary(nums,0,len(nums)-1)
    
    def binary(self,nums,l,r):
        while l<=r:
            mid = l + (r-l)//2
            if (mid == 0 or nums[mid]>=nums[mid-1]) and (mid == len(nums)-1 or nums[mid]>=nums[mid+1]):
                return mid
            elif mid>0 and nums[mid-1]>nums[mid]:
                r = mid-1
            else:
                l = mid+1