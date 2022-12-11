class Solution:
    def binarysearch(self,nums,x):
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==x:
                return mid
            elif nums[mid]>x:
                high = mid-1
            else:
                low = mid+1
        return -1
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxl = -1
        print(nums)
        for n in nums:
            l = 1
            x = n
            while self.binarysearch(nums,x**2) != -1:
                    # print(x**2,'found')
                    l+=1
                    x = x**2
            if l>=2:
                maxl = max(maxl,l)
        return maxl
            
            
        