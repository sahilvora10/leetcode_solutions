class Solution:
    def dfs(self,i,j,visited,n_rows,n_cols,grid,possible_dir):
        visited[i][j] = 1
        for p in possible_dir:
            r = i+p[0]
            c = j+p[1]
            if r>=0 and r<n_rows and c>=0 and c<n_cols and visited[r][c]!=1 and grid[r][c]==1:
                
                self.dfs(r,c,visited,n_rows,n_cols,grid,possible_dir)
                
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        visited = [[0 for i in range(n_cols)] for j in range(n_rows)]
        possible_dir = [[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(n_cols):
            if grid[0][i] == 1 and visited[0][i]!=1:
                self.dfs(0,i,visited,n_rows,n_cols,grid,possible_dir)
            if grid[n_rows-1][i] == 1 and visited[n_rows-1][i]!=1:
                self.dfs(n_rows-1,i,visited,n_rows,n_cols,grid,possible_dir)
        for i in range(n_rows):
            if grid[i][0] == 1 and visited[i][0]!=1:
                self.dfs(i,0,visited,n_rows,n_cols,grid,possible_dir)
            if grid[i][n_cols-1] == 1 and visited[i][n_cols-1]!=1:
                self.dfs(i,n_cols-1,visited,n_rows,n_cols,grid,possible_dir)
        count = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if visited[i][j] != 1 and grid[i][j] == 1:
                    count += 1
        return count
        