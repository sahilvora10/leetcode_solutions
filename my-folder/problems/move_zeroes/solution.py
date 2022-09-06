def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # if n != 1:
        #     i = 0
        #     for i in range(n):
        #         if nums[i] == 0:
        #             break
        #         else:
        #             i +=1
        #     s = i
        #     j = i+1
        #     while s<n and j<n:
        #         if nums[s] == 0 and nums[j]!=0:
        #             swap(nums,s,j)
        #             i+=1
        #             j+=1
        #         elif nums[j] == 0:
        #             j+=1
        #         else:
        #             continue
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
