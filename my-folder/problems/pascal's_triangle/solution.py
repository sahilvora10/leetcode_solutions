class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        solution = [[1]]
        for rows in range(1,numRows):
            a = [1]*(rows+1)
            if rows>=2:
                for i in range(1,rows):
                    a[i] = solution[rows-1][i-1] + solution[rows-1][i]
            solution.append(a)
        return solution
            
            
        