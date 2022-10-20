class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxvol = -1
        while l<r:
            vol = min(height[l],height[r])*(r-l)
            print(height[l],height[r],vol)
            maxvol = max(maxvol,vol)
            if height[l]<height[r]:
                l +=1
            else:
                r -= 1
        return maxvol
        