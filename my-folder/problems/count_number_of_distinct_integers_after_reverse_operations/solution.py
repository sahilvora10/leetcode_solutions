class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            x = nums[i]
            revx = int(str(x)[::-1])
            nums.append(revx)
        print(nums)
        return len(set(nums))