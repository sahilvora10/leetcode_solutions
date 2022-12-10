class Solution:
    def maxJump(self, stones: List[int]) -> int:
        res = stones[1]-stones[0]
        for i in range(2,len(stones)):
            x = (stones[i]-stones[i-1])+(stones[i-1]-stones[i-2])
            res = max(res,x)
        return res
        