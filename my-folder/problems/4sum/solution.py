class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for f in range(len(nums)):
            if f>0 and nums[f] == nums[f-1]:
                continue
            tf = target - nums[f]
            for k in range(f+1,len(nums)):
                if k>f+1 and nums[k] == nums[k-1]:
                    continue
                tt = tf-nums[k]

                i = k+1
                j = len(nums)-1
                while i<j:
                    s = nums[i]+nums[j]
                    if  s == tt:
                        res.append([nums[f],nums[k],nums[i],nums[j]])
                        i+=1
                        while nums[i] == nums[i-1] and i<j:
                            i+=1
                    elif s>tt:
                        j = j-1
                    else:
                        i = i+1
        return res
        