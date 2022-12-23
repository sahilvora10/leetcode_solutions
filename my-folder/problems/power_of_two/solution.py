class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # binary = list(bin(n)[2:])
        # if binary[0] == '1' and '1' not in binary[1:]:
        #     return True
        # return False
        if n and n&(n-1)==0:
            return True
        return False
        