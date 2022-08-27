class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # c = nums.count(val)
        # for i in range(c):
        #     nums.remove(val)
        # print(len(nums))
        i = 0
        for n in nums:
            if n == val:
                continue
            nums[i] = n
            i += 1
        return i
        