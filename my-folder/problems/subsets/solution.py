class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub_seq(i,arr):
            if i >= len(nums):
                output.append(list(arr))
                return
            arr.append(nums[i])
            sub_seq(i+1,arr)
            arr.remove(nums[i])
            sub_seq(i+1,arr)
        output = []
        arr = []
        sub_seq(0,arr)
        return output
        
        