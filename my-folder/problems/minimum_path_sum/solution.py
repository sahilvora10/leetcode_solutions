class Solution:
    def recursivesol(self,i,j,grid):
        if i==0 and j==0:
            return grid[i][j]
        if i==-1 or j==-1:
            return 100000001
        up = grid[i][j]+self.recursivesol(i-1,j,grid)
        left = grid[i][j]+self.recursivesol(i,j-1,grid)
        return min(up,left)

    def memo(self,i,j,dp,grid):
        if i==0 and j==0:
            return grid[i][j]
        if i==-1 or j==-1:
            return 100000001
        if dp[i][j] != -1:
            # print("here")
            return dp[i][j]
        up = grid[i][j]+self.memo(i-1,j,dp,grid)
        left = grid[i][j]+self.memo(i,j-1,dp,grid)
        dp[i][j]=min(up,left)
        return min(up,left)
    
    def tab(self,m,n,grid):
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                else:
                    up,left = grid[i][j],grid[i][j] 
                    if i>0:
                        up += dp[i-1][j]
                    else:
                        up += 10000001
                    if j>0:
                        left += dp[i][j-1]
                    else:
                        left += 1000001
                    dp[i][j] = min(up,left)
        return dp[m-1][n-1]
                        
    
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # return self.recursivesol(m-1,n-1,grid)
        # dp = [[-1 for j in range(n)] for i in range(m)]
        # return self.memo(m-1,n-1,dp,grid)
        return self.tab(m,n,grid)