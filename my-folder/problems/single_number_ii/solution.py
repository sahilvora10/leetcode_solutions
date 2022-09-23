class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using an extra memory
        hashkey = {}
        for n in nums:
            if n in hashkey:
                hashkey[n] += 1
            else:
                hashkey[n] = 1
        for k,v in hashkey.items():
            if v == 1:
                return k
        return -1
        
        # c = Counter(nums)
        # for k,v in c.items():
        #     if v == 1:
        #         return k
        
        #without extra memory
        
    