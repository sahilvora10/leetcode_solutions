class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        ceil = -1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                ceil = mid
                break
            elif target>nums[mid]:
                l = mid+1
            else:
                ceil = mid
                r = mid-1
        return ceil if ceil != -1 else len(nums)
        