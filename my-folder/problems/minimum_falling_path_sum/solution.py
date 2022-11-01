class Solution:
#     def rec(self,matrix,i,j,n):
#         # print(i,j)
#         if i==n-1:
#             return matrix[i][j]
#         right = matrix[i][j] + self.rec(matrix,i+1,j-1,n) if j>0 else 100001
#         down =  matrix[i][j] + self.rec(matrix,i+1,j,n)
#         left =  matrix[i][j] + self.rec(matrix,i+1,j+1,n) if j<n-1 else 100001
#         # print(right,down,left)
#         return min(right,min(down,left))
    
#     def memo(self,matrix,i,j,n,dp):
#         # print(i,j)
#         if i==n-1:
#             return matrix[i][j]
#         if dp[i][j] != -1: return dp[i][j]
#         right = matrix[i][j] + self.memo(matrix,i+1,j-1,n,dp) if j>0 else 100001
#         down =  matrix[i][j] + self.memo(matrix,i+1,j,n,dp)
#         left =  matrix[i][j] + self.memo(matrix,i+1,j+1,n,dp) if j<n-1 else 100001
#         dp[i][j] = min(right,min(down,left))
#         return min(right,min(down,left))
    
#     def tab(self,matrix):
#         n = len(matrix)
#         dp = [[0 for i in range(n)] for j in range(n)]
#         for i in range(n):
#             dp[n-1][i] = matrix[n-1][i]
#         for i in range(n-2,-1,-1):
#             for j in range(n):
#                 right = matrix[i][j] + dp[i+1][j-1] if j>0 else 100001
#                 down =  matrix[i][j] + dp[i+1][j]
#                 left =  matrix[i][j] + dp[i+1][j+1] if j<n-1 else 100001
#                 dp[i][j] = min(right,min(down,left))
#         minres = 1000001
#         for i in range(0,n):
#             minres = min(minres,dp[0][i])
#         return minres
    
    def spaceoptab(self,matrix):
        n = len(matrix)
        prev = [0 for i in range(n)]
        for i in range(n):
            prev[i] = matrix[n-1][i]
        for i in range(n-2,-1,-1):
            curr = [0 for k in range(n)]
            for j in range(n):
                right = matrix[i][j] + prev[j-1] if j>0 else 100001
                down =  matrix[i][j] + prev[j]
                left =  matrix[i][j] + prev[j+1] if j<n-1 else 100001
                curr[j] = min(right,min(down,left))
            prev = curr
        return min(prev)
        
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # minres = 1000001
        # n = len(matrix)
        # dp = [[-1 for i in range(n)] for j in range(n)]
        # for i in range(0,n):
        #     minres = min(minres,self.memo(matrix,0,i,len(matrix),dp))
        # return minres
        # return self.tab(matrix)
        return self.spaceoptab(matrix)