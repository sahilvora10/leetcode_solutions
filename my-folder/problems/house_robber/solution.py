class Solution:
    
    def dpspace(self,arr,n):
        prev2 = 0
        prev1 = arr[0]
        curr = -1
        for i in range(1,n):
            pick = arr[i]
            if i>1:
                pick += prev2
            notpick = prev1
            curr = max(pick,notpick)
            prev2 = prev1
            prev1 = curr
        return prev1
    
    def rob(self, nums: List[int]) -> int:
        return self.dpspace(nums,len(nums))
        