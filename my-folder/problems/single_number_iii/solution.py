class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for n in nums:
            hashmap[n] = hashmap[n]+1 if n in hashmap else 1
        for k,v in hashmap.items():
            print(k,v)
            if v==1:
                res.append(k)
        return res
        
        
        