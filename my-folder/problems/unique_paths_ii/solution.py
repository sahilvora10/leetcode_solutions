class Solution:
    def recursivesol(self,i,j,obstacleGrid):
        if i>=0 and j>=0 and obstacleGrid[i][j]==1:
            return 0
        if i==0 and j==0:
            return 1
        if i==-1 or j==-1:
            return 0
        up = self.recursivesol(i-1,j,obstacleGrid)
        left = self.recursivesol(i,j-1,obstacleGrid)
        return up+left
    
    def memo(self,i,j,dp,obstacleGrid):
        if i>=0 and j>=0 and obstacleGrid[i][j]==1:
            return 0
        if i==0 and j==0:
            return 1
        if i==-1 or j==-1:
            return 0
        if dp[i][j] != -1:
            # print("here")
            return dp[i][j]
        up = self.memo(i-1,j,dp,obstacleGrid)
        left = self.memo(i,j-1,dp,obstacleGrid)
        dp[i][j]=up+left
        return up+left
    
    def tab(self,m,n,obstacleGrid):
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                up,left = 0,0
                if obstacleGrid[i][j] == 1:
                    dp[i][j]=0
                elif i ==0 and j==0:
                    dp[0][0] = 1
                else:
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]

                    dp[i][j] = up+left
                    # print(i,j,dp[i][j])
        return dp[m-1][n-1]
    
    def spaceoptab(self,m,n,obstacleGrid):
        prev = [0 for j in range(n)]
        for i in range(m):
                curr = [0 for j in range(n)]
                for j in range(n):
                    if obstacleGrid[i][j] == 1:
                        curr[j]=0
                    elif i ==0 and j==0:
                        curr[0] = 1
                    else:
                        curr[j] = prev[j]+curr[j-1]
                prev = curr
        return prev[n-1]
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # return self.recursivesol(len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # dp = [[-1 for j in range(n)] for i in range(m)]
        # return self.memo(m-1,n-1,dp,obstacleGrid)
        # return self.tab(m,n,obstacleGrid)
        return self.spaceoptab(m,n,obstacleGrid)