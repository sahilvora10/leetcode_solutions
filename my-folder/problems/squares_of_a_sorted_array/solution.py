class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0]*l
        lo = 0
        hi = l-1
        index = l-1
        while (lo<=hi):
            if abs(nums[lo])<abs(nums[hi]):
                res[index] = nums[hi]**2
                # print(res[index])
                index -=1
                hi -= 1
            else:
                res[index] = nums[lo]**2
                index -=1
                lo +=1
        return res
        