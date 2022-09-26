class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        r = ((n+1)*(n))//2
        return r-sum(nums)
            
        
        