class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for c in queries:
            x2 = c[0]
            y2 = c[1]
            rad = c[2]
            count = 0
            for p in points:
                x1 = p[0]
                y1 = p[1]
                if (x1-x2)**2 + (y1-y2)**2 <= rad**2:
                    count+=1
            ans.append(count)
        return ans
            
                