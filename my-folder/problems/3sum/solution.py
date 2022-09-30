class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # for i in range(len(nums)):
        #     hm = set()
        #     target = -nums[i]
        #     for j in range(i+1,len(nums)):
        #         rem = target-nums[j]
        #         if rem in hm:
        #             res.append([nums[i],nums[j],rem])
        #         hm.add(nums[j])
        # return res
        nums = sorted(nums)
        for k in range(len(nums)-2):
            if k>0 and nums[k] == nums[k-1]:
                continue
            target = -nums[k]
            
            i = k+1
            j = len(nums)-1
            while i<j:
                s = nums[i]+nums[j]
                if  s == target:
                    res.append([nums[k],nums[i],nums[j]])
                    i+=1
                    while nums[i] == nums[i-1] and i<j:
                        i+=1
                elif s>target:
                    j = j-1
                else:
                    i = i+1
        return res

            
                    
            
        