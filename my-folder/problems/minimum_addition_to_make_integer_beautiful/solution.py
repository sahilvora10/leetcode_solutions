class Solution:
    def sumofdigits(self,n):
        s = 0
        st = str(n)
        for i in st:
            s += int(i)
        return s
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        res = 0
        sol = 0
        i=1
        while(True):
            if self.sumofdigits(n) <= target:
                return sol
            res = (10**i- n%(10**i))
            n += res
            sol += res 
            i+=1
            print(n)
        