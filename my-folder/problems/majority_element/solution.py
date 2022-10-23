class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #brute force
        # hm = {}
        # for n in nums:
        #     if n in hm:
        #         hm[n]+=1
        #         if hm[n]>(len(nums)//2):
        #             return n
        #     else:
        #         hm[n] = 1
        # return nums[0]
        #moore voting algo
        count = 0
        element = 0
        for i in range(len(nums)):
            if count == 0:
                element=nums[i]
            if element == nums[i]:
                count+=1
            else:
                count-=1
        return element