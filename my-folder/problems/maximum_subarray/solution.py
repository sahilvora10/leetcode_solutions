class Solution:
    
    # def recursivefunction(self,nums,i):
    #     global globalmax
    #     if i==0:
    #         globalmax = max(nums[0],globalmax)
    #         return nums[0]
    #     r = max(nums[i],nums[i]+self.recursivefunction(nums,i-1))
    #     globalmax = max(r,globalmax)
    #     return r
    
    # def memosol(self,nums,i,dp):
    #     global globalmax
    #     if i == 0:
    #         globalmax = max(nums[0],globalmax)
    #         return nums[0]
    #     if dp[i-1]!=None:
    #         return dp[i-1]
    #     dp[i] = max(nums[i],nums[i]+self.memosol(nums,i-1,dp))
    #     globalmax = max(dp[i],globalmax)
    #     return dp[i]
    
    # def tabulation(self,nums):
    #     dp = [None]*len(nums)
    #     dp[0] = nums[0]
    #     for i in range(1,len(nums)):
    #         dp[i] = max(nums[i],nums[i]+dp[i-1])
    #     return max(dp)
    
    def spaceoptabulation(self,nums):
        prev = nums[0]
        curr = -10000
        globalmax = nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i],nums[i]+prev)
            globalmax = max(globalmax,curr)
            prev = curr
        return globalmax
    
    def maxSubArray(self, nums: List[int]) -> int:
        # global globalmax
        # globalmax = -100000
        # dp = [None]*len(nums)
        if len(nums) == 1:
            return nums[0]
        # self.memosol(nums,len(nums)-1,dp)
        # self.recursivefunction(nums,len(nums)-1)
        # return globalmax
        # return self.tabulation(nums)
        return self.spaceoptabulation(nums)