class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        sol = 0
        for i in range(r):
            grid[i] = sorted(grid[i],reverse=True)
        for i in range(c):
            maxc = -1
            for j in range(r):
                if grid[j][i]>=maxc:
                    maxc = grid[j][i]
            # print(maxc)
            sol+=maxc
        return sol
        