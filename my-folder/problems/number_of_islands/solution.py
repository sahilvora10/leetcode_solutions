class Solution:
    def bfs(self,i,j,grid,visited,n_rows,n_cols,possible_dir):
        visited[i][j] = 1
        
        queue = []
        queue.append([i,j])
        while len(queue)>0:
            [r,c] = queue.pop(0)
            # print(r,c)
            for p in possible_dir:
                k,l = p[0],p[1]
                n_r = r+k
                n_c = c+l
                if n_r>=0 and n_r<n_rows and n_c>=0 and n_c<n_cols and grid[n_r][n_c] == '1' and visited[n_r][n_c] !=1:
                    queue.append([n_r,n_c])
                    visited[n_r][n_c] = 1
                    
    def dfs(self,i,j,grid,visited,n_rows,n_cols,possible_dir):
        visited[i][j] = 1
        for p in possible_dir:
            k,l = p[0],p[1]
            n_r = i+k
            n_c = j+l
            if n_r>=0 and n_r<n_rows and n_c>=0 and n_c<n_cols and grid[n_r][n_c] == '1' and visited[n_r][n_c] !=1:
                self.dfs(n_r,n_c,grid,visited,n_rows,n_cols,possible_dir)

        
                        
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        possible_dir = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = [[0 for i in range(n_cols)] for j in range(n_rows)]
        count = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '1' and visited[i][j]!=1:
                    count+=1
                    # print(count)
                    # self.bfs(i,j,grid,visited,n_rows,n_cols,possible_dir)
                    self.dfs(i,j,grid,visited,n_rows,n_cols,possible_dir)
        return count
                    
                
                