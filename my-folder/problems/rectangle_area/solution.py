class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = (ax2-ax1)*(ay2-ay1)
        # print(a1)
        a2 = (bx2-bx1)*(by2-by1)
        # print(a2)
        left = max(ax1,bx1)
        right = min(ax2,bx2)
        top = min(ay2,by2)
        bottom = max(ay1,by1)
        overlap = 0
        if right>left and top>bottom:
            overlap = ((right-left)*(top-bottom))
        # print(overlap)
        return a1+a2-overlap
        