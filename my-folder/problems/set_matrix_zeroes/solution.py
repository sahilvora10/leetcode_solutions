class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zr = False
        zc = False
        for i in range(0,m):
            for j in range(0,n):
                if (matrix[i][j] == 0):
                    if i==0:
                        zr = True 
                    if j ==0:
                        zc = True
                    matrix[i][0] = matrix[0][j] = 0
        print(matrix)
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if zr:
            for j in range(n):
                matrix[0][j]=0
        
        if zc:
            for i in range(m):
                matrix[i][0]=0
        
    
                    
        