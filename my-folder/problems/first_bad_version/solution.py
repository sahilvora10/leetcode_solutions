# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binary(0,n)
    
    def binary(self,a,b):
            if a>=b:
                return a
            mid = (a+b)//2
            if (isBadVersion(mid)):
                return self.binary(0,mid)
            else:
                return self.binary(mid+1,b)
            
        
        