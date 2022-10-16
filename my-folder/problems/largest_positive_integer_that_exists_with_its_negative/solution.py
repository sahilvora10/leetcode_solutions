class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxres = -1
        for n in nums:
            if n>0 and -n in nums:
                maxres = max(maxres,n)
        return maxres
        