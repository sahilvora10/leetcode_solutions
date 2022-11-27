class Solution:
    def pivotInteger(self, n: int) -> int:
        z = int((n**2+n)/2)
        x = int(sqrt(z))
        if z==x*x:
            return x
        else:
            return -1
        