class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        # while n%3 == 0:
        #     n = n/3
        # return n == 1
        # return 3**(round(math.log(n,3))) == n
        return 3**19%n == 0
            