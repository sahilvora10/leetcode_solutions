class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = 1
        for i in range(1,(x//2)+1):
            if i*i == x:
                return i
            elif i*i<x:
                ans = i
            elif i*i>x:
                return ans
        return ans
        