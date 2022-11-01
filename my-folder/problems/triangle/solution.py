class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev = [0 for i in range(n)]
        for i in range(n):
            prev[i] = triangle[n-1][i]
        for i in range(n-2,-1,-1):
            curr = [0 for k in range(i+1)]
            for j in range(i+1):
                curr[j] = triangle[i][j] + min(prev[j],prev[j+1])
            prev = curr
        return prev[0]
        