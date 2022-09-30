class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hp = {}
        res = 0
        for i,n in enumerate(nums1):
            for j,k in enumerate(nums2):
                s = n+k
                if s not in hp:
                    hp[s] = 1
                else:
                    hp[s] += 1
        print(hp)
        
        for i,n in enumerate(nums3):
            for j,k in enumerate(nums4):
                s = -(n+k)
                if s in hp:
                    res += hp[s]
        return res
                    
        
        