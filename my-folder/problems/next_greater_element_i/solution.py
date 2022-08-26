class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # for n in nums1:
        #     i = nums2.index(n)
        #     flag = False
        #     for j in range(i,len(nums2)):
        #         print(j)
        #         if nums2[j]>n:
        #             ans.append(nums2[j])
        #             flag = True
        #             break;
        #     if flag == False:
        #         ans.append(-1)
        # return ans
        mapkey = {}
        stack = []
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapkey[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        ans = []
        for i in stack:
            mapkey[i] = -1
            
        for n in nums1:
            ans.append(mapkey[n])
            
        return ans
                
                    