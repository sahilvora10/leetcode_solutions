class Solution:
    def bfs(self,grid,visited,n_rows,n_cols,queue):
        possible_dir = [[-1,0],[1,0],[0,-1],[0,1]]
        maxtime = 0
        cnt = 0
        while len(queue)>0:
            [i,j,t] = queue.pop(0)
            maxtime = t
            for p in possible_dir:
                r = i+p[0]
                c = j+p[1]
                if r>=0 and r<n_rows and c>=0 and c<n_cols and grid[r][c] == 1 and visited[r][c]!=1:
                    queue.append([r,c,t+1])
                    visited[r][c] = 1
                    cnt+=1
            # print(queue)
            
        return maxtime,cnt
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        visited = [[0 for i in range(n_cols)] for j in range(n_rows)]
        queue = []
        cntfresh = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 2:
                    queue.append([i,j,0])
                elif grid[i][j] == 1:
                    cntfresh+=1
        # print(cntfresh)
        maxtime,cnt = self.bfs(grid,visited,n_rows,n_cols,queue)
        # print(cnt)
        if cntfresh==cnt:
            return (maxtime)
        else:
            return -1
        