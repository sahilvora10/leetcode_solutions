class Solution:
    def minOperations(self, n: int) -> int:
        #manually
        # nums = [(2*i)+1 for i in range(n)]
        # print(nums)
        # mean = sum(nums)//len(nums)
        # print(mean)
        # c = 0
        # for i in range(len(nums)//2):
        #     c += (mean-nums[i])
        # return c
        #matehmatically
        # x = n//2
        # return (x*n - x*x)
        # simplifying
        return (n*n)//4
            
        