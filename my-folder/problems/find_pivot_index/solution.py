class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # totalsum = sum(nums)
        # print(totalsum)
        # runningsum = nums.copy()
        # for i in range(1,len(nums)):
        #     runningsum[i] = runningsum[i] + runningsum[i-1]
        # print(runningsum)
        # for i in range(0,len(nums)):
        #     if runningsum[i]-nums[i] == totalsum-runningsum[i]:
        #         return i
        #     print("Left Sum ",runningsum[i]-nums[i])
        #     print("Right Sum",totalsum-runningsum[i])
        # return -1
        l = 0
        r = sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]
        return -1
            
        