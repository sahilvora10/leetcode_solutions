class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        res = []
        res.append(self.biased_binary(nums,l,r,target,'left'))
        res.append(self.biased_binary(nums,l,r,target,'right'))
        return res
    
    def biased_binary(self,nums,l,r,target,biased):
        i = -1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid -1
            else:
                i =  mid
                if biased == 'left':
                    r =  mid-1
                else:
                    l = mid+1
        return i