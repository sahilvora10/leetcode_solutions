class Solution:
    
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n_rows = len(maze)
        n_cols = len(maze[0])
        visited = [[-1 for i in range(n_cols)] for j in range(n_rows)]
        possible_dir = [[-1,0],[1,0],[0,-1],[0,1]]
        queue = deque()
        queue.append([entrance[0],entrance[1],0])
        visited[entrance[0]][entrance[1]] = 1
        while len(queue)>0:
            [i,j,d] = queue.popleft()
            for p in possible_dir:
                r = i+p[0]
                c = j+p[1]
                if r>=0 and r<n_rows and c>=0 and c<n_cols and maze[r][c]=='.' and visited[r][c]!=1:
                    queue.append([r,c,d+1])
                    visited[r][c] = 1
                    if r==n_rows-1 or r==0 or c ==0 or c==n_cols-1:
                        return d+1
        return -1
        