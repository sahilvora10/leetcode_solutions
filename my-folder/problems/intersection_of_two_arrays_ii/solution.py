class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        key = {}
        res = []
        for i in nums1:
            key[i] = key[i] + 1 if i in key else 1
        print(key)
        for j in nums2:
            if j in key and key[j]>0:
                res.append(j)
                key[j] -= 1
        return res