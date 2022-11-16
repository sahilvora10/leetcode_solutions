class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        boundary = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count+=1
                    if j<len(grid[0])-1 and grid[i][j+1] == 1:
                        boundary+=1
                    if i<len(grid)-1 and grid[i+1][j] == 1:
                        boundary+=1
        return count*4 - boundary*2       
        
                    
        