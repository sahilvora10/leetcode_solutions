class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        #brute force
        # count = 0 
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         for k in range(j,len(nums)):
        #             if nums[k]-nums[j] == diff and nums[j]-nums[i] == diff:
        #                 count+=1
        # return count
        s = set(nums)
        count=0
        for n in nums:
            if n+diff in s and n+(2*diff) in s:
                count+=1
        return count
        
    
        