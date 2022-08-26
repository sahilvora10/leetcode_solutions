class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lmax = 0
        l = 0
        for i in nums:
            if i == 0:
                l = 0
            else:
                l += 1
                lmax = max(l,lmax)
        return lmax
        