import collections
class Solution:
    def bfs(self,n_rows,n_cols,visited,distance,queue):
        possible_dir = [[-1,0],[1,0],[0,1],[0,-1]]
        while len(queue)>0:
            i,j,d = queue.popleft()
            distance[i][j] = d
            for p in possible_dir:
                r = i+p[0]
                c = j+p[1]
                if r>=0 and r<n_rows and c>=0 and c<n_cols and visited[r][c]!=1:
                    # print(r,c)
                    queue.append((r,c,d+1))
                    visited[r][c] = 1
    
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n_rows = len(mat)
        n_cols = len(mat[0])
        queue = collections.deque()
        visited = [[0 for i in range(n_cols)] for j in range(n_rows)]
        distance = [[0 for i in range(n_cols)] for j in range(n_rows)]
        for i in range(n_rows):
            for j in range(n_cols):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited[i][j] = 1
        self.bfs(n_rows,n_cols,visited,distance,queue)
        return distance
        
        