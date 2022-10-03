class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0,len(nums)-1,nums,target)
    
    def binary_search(self,l,r,nums,target):
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[l]<=nums[mid]:
                if target>=nums[l] and target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target>=nums[mid] and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid -1
        return -1
    