class Solution:
#     def rec(self,matrix,i,j,n):
#         # print(i,j)
#         if i==n-1:
#             return matrix[i][j]
#         minval = 1000001
#         for k in range(n):
#             if k!=j:
#                 value_i_k = matrix[i][j]+self.rec(matrix,i+1,k,n)
#                 minval = min(minval,value_i_k)
#         return minval
    
#     def memo(self,matrix,i,j,n,dp):
#         # print(i,j)
#         if i==n-1:
#             return matrix[i][j]
#         if dp[i][j] != -1:
#             return dp[i][j]
#         minval = 1000001
#         for k in range(n):
#             if k!=j:
#                 value_i_k = matrix[i][j]+self.memo(matrix,i+1,k,n,dp)
#                 minval = min(minval,value_i_k)
#         dp[i][j] = minval
#         return minval
    
    # def tab(self,matrix):
    #     n = len(matrix)
    #     dp = [[0 for i in range(n)] for j in range(n)]
    #     for i in range(n):
    #         dp[n-1][i] = matrix[n-1][i]
    #     for i in range(n-2,-1,-1):
    #         for j in range(n):
    #             minval = 10000000001
    #             for k in range(n):
    #                 if k!=j:
    #                     value_i_k = matrix[i][j] + dp[i+1][k]
    #                     minval = min(minval,value_i_k)
    #             dp[i][j] = minval
    #     minres = 1000001
    #     for i in range(0,n):
    #         minres = min(minres,dp[0][i])
    #     return minres
    
    def getmins(self,arr):
        min1,min2 = 10000000001,1000000001
        for num in arr:
            if num<min1:
                min2 = min1
                min1 = num
            elif num<min2:
                min2 = num
        return (min1,min2)
        
    
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # minres = 1000001
        n = len(grid)
        # dp = [[-1 for i in range(n)] for j in range(n)]
        # for i in range(0,n):
        #     minres = min(minres,self.memo(grid,0,i,len(grid),dp))
        # return self.tab(grid)
        min1,min2 = self.getmins(grid[n-1])
        for i in range(n-2,-1,-1):
            print(min1,min2)
            for j in range(n):
                if min1 == grid[i+1][j]:
                    grid[i][j] += min2
                else:
                    grid[i][j]+=min1
            min1,min2 = self.getmins(grid[i])
        return min1
                
            
        