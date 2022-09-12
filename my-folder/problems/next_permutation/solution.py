class Solution:
    
    
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(nums,i,j):
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
        """
        Do not return anything, modify nums in-place instead.
    
        """
        n  = len(nums)
        i1 = 0
        i2 = 0
        flag = False
        for i in range(n-1,0,-1):
            # print(nums[i-1]," ",nums[i])
            if nums[i-1]<nums[i]:
                i1 = i-1
                flag = True
                break
        if not flag:
            i1 = -1
            for i in range(i1+1,n):
                t = nums.pop()
                nums.insert(i,t)
            
        else:
            for i in range(n-1,0,-1):
                if nums[i]>nums[i1]:
                    i2 = i
                    break
            swap(nums,i1,i2)
            for i in range(i1+1,n):
                t = nums.pop()
                nums.insert(i,t)
        
        
        
        
        
        print(nums)
                