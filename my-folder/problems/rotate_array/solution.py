def reverse_arr(arr,start,end):
    while (start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # a = [0]*len(nums)
        # for i in range(len(nums)):
        #     a[(i+k)%len(nums)] = nums[i]
        # for i in range(len(nums)):
        #     nums[i] = a[i]
        n = len(nums)
        if k>n:
            k = k%n
            # print(k)
        reverse_arr(nums,n-k,n-1)
        print(nums)
        reverse_arr(nums,0,n-k-1)
        print(nums)
        reverse_arr(nums,0,n-1)
        print(nums)