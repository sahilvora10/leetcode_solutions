class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return (bin(x^y).count("1"))
        xor = x ^ y
        ham = 0
        while xor != 0:
            ham += xor & 1 # or ham += xor%2
            xor >>= 1
        return ham
        