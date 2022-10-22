class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for n in nums:
            if n in hm:
                hm[n]+=1
                if hm[n]>(len(nums)//2):
                    return n
            else:
                hm[n] = 1
        return nums[0]
        