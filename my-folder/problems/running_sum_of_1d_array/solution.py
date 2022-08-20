class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # print(nums)
        # print(x)
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums