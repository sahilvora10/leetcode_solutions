class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = nums[0]
        for n in nums[1:]:
            r = r^n
        return r
        