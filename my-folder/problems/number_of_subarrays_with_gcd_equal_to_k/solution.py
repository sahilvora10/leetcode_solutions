from math import gcd
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            curr_gcd = 0
            for j in range(i,len(nums)):
                curr_gcd = gcd(curr_gcd,nums[j])
                if curr_gcd == k:
                    res+=1
        return res
        
        