class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        mem = []
        for i in range(0,m):
            for j in range(0,n):
                if (matrix[i][j] == 0):
                    mem.append([i,j])
        # print(mem)
        for point in mem:
            for k in range(0,m):
                # print (k,point[1])
                matrix[k][point[1]] = 0
            for k in range(0,n):
                matrix[point[0]][k] = 0
                    
        