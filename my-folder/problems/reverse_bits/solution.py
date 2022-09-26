class Solution:
    def reverseBits(self, n: int) -> int:
        
        # x = '{0:032b}'.format(n)
        # x = x[::-1]
        # print(x)
        # return (int(x,2))
        res = 0
        for i in range(0, 32):
            print(res,n)
            res = res << 1
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res
        