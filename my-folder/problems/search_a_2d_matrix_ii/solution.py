class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #start from top rightcorner
        #if target greater than that then not in that row as its highest in that row
        #if target smaller than that then not in that col as its the smallest in that row
        
        nr = len(matrix)
        nc = len(matrix[0])
        r = 0
        c = nc-1
        while c>=0 and r<nr:
            if target==matrix[r][c]:
                return True
            elif target>matrix[r][c]:
                r+=1
            else:
                c-=1
        return False