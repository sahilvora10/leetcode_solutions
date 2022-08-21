class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ans =[]
        # for i in range(0,len(nums)):
        #     if target-nums[i] in nums:
        #         j = nums.index(target-nums[i])
        #         if i!=j:
        #             ans.append(i)
        #             ans.append(j)
        #             return ans
        seen = {}
        for i,value in enumerate(nums):
            rem = target - value
            if rem in seen:
                return [i,seen[rem]]
            else:
                seen[value]=i