class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        globalSum = nums[0]
        
        if len(nums) < 1:
            return globalsum
        
        for i in range(1, len(nums)):
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
                
            if current > globalSum:
                globalSum = current
                
        return globalSum 