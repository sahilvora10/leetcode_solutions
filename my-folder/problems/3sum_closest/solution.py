class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
        minres = 10**5
        nums = sorted(nums)
        print(nums)
        ans = -1
        for k in range(len(nums)-2):
            target = t-nums[k]
            i = k+1
            j = len(nums)-1
            while i<j:
                s = nums[i]+nums[j]
                if  s == target:
                    return s+nums[k]
                elif s>target:
                    if minres>abs(target-s):
                        minres = abs(target-s)
                        ans = nums[k]+nums[i]+nums[j]
                    j = j-1
                else:
                    if minres>abs(target-s):
                        minres = abs(target-s)
                        ans = nums[k]+nums[i]+nums[j]
                    i = i+1
        return ans
        