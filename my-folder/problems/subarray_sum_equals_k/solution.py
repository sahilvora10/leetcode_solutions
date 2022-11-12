class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #brute force
        # running_sum = [0]*(len(nums)+1)
        # running_sum[0] = 0
        # for i in range(1,len(nums)+1):
        #     running_sum[i] = running_sum[i-1]+nums[i-1]
        # print(running_sum)
        # count = 0
        # for i in range(len(running_sum)):
        #     for j in range(i+1,len(running_sum)):
        #         if running_sum[j] - running_sum[i] == k:
        #             count+=1
        # return count
        hp = {}
        hp[0] = 1
        count = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if (s-k) in hp:
                count+=hp[s-k]
            hp[s] = hp.get(s,0) + 1
        return count
            
        
                
                
        