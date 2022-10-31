class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s,c = 0,0
        for n in nums:
            if n%6 == 0:
                c += 1
                s += n
        print(c,s)
        return s//c if c>0 else 0
        