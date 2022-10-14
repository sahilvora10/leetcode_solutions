class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        hp = {}
        for n in nums:
            if n in hp:
                hp[n]+=1
            else:
                hp[n] = 1
        print(hp)
        for i in hp.values():
            if i>1:
                ans += (i*(i-1))//2
        return ans
        