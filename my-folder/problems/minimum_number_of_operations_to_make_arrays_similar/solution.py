
from itertools import permutations
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        #brute force
#         minans = 10**6+1
#         nums = sorted(nums)
#         if set(nums) == set(target):
#             return 0
#         l = list(permutations(target))
#         for x in l:
#             s = 0
#             for i in range(len(nums)):
#                 s += abs(nums[i]-x[i])
#             if s%4 == 0:
#                 minans = min(minans,s//4)
#         return minans
        nums = sorted(nums)
        target = sorted(target)
        oddn,evenn,oddt,event = [],[],[],[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                evenn.append(nums[i])
            else:
                oddn.append(nums[i])
            if target[i]%2==0:
                event.append(target[i])
            else:
                oddt.append(target[i])
        print(oddn,evenn,oddt,event)
        count = 0
        for i in range(len(oddn)):
            if oddn[i]<oddt[i]:
                count += (oddt[i]-oddn[i])//2
        for i in range(len(evenn)):
            if evenn[i]<event[i]:
                count += (event[i]-evenn[i])//2
        return count
                
                    
                