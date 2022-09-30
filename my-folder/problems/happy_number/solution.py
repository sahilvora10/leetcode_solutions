class Solution:

    def isHappy(self, n: int) -> bool:
        
        hm = set()
        hm.add(n)
        while True:
            n = self.sumdigit(n)
            if n == 1:
                return True
            if n in hm:
                return False
            else:
                hm.add(n)
            
        
            
        
    def sumdigit(self,n):
        s = 0
        while n>0:
            s += (n%10)**2
            n = n//10
        return s
        
        