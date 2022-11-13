from math import gcd
class Solution:
    def subarrayLCM(self, nums: List[int], tar: int) -> int:
        count = 0
        for i in range(len(nums)):
            lcm = nums[i]
            for j in range(i,len(nums)):
                lcm = (nums[j]*lcm)//gcd(nums[j],lcm)
                # print(i,j,lcm)
                if lcm == tar:
                    count+=1  
        return count
                
        