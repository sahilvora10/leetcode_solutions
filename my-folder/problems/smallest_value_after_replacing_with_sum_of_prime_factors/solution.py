class Solution:
    
        
    def smallestValue(self, n: int) -> int:
        def primeFactors(n):
            c = 2
            sum_prime=0
            while(n > 1):

                if(n % c == 0):
                    # print(c, end=" ")
                    sum_prime+=c
                    n = n / c
                else:
                    c = c + 1
            return sum_prime
        oldn = 0
        minsp = 1000000001
        while oldn!=n:
            # print(oldn,n)
            oldn = n
            sp = primeFactors(n)
            # print(sp)
            minsp = min(minsp,sp)
            n = sp
        return minsp
        