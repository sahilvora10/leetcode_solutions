class Solution:
    def recursivesol(self,i,j):
        if i==0 and j==0:
            return 1
        if i==-1 or j==-1:
            return 0
        up = self.recursivesol(i-1,j)
        left = self.recursivesol(i,j-1)
        return up+left
    
    def memo(self,i,j,dp):
        if i==0 and j==0:
            return 1
        if i==-1 or j==-1:
            return 0
        if dp[i][j] != -1:
            # print("here")
            return dp[i][j]
        up = self.memo(i-1,j,dp)
        left = self.memo(i,j-1,dp)
        dp[i][j]=up+left
        return up+left
    
    def tab(self,m,n):
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                up,left = 0,0
                if i ==0 and j==0:
                    dp[0][0] = 1
                else:
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]

                    dp[i][j] = up+left
                    # print(i,j,dp[i][j])
        return dp[m-1][n-1]
    
    def spaceoptab(self,m,n):
        prev = [0 for j in range(n)]
        for i in range(m):
                curr = [0 for j in range(n)]
                for j in range(n):
                    if i ==0 and j==0:
                        curr[0] = 1
                    else:
                        curr[j] = prev[j]+curr[j-1]
                prev = curr
        return prev[n-1]

    
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.recursivesol(m-1,n-1)
        dp = [[-1 for j in range(n)] for i in range(m)]
        # return self.memo(m-1,n-1,dp)
        # return self.tab(m,n)
        return self.spaceoptab(m,n)