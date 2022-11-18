class Solution:
    def dfs(self,i,j,visited,n_rows,n_cols,board,possible_dir):
        visited[i][j] = 1
        for p in possible_dir:
            r = i+p[0]
            c = j+p[1]
            if r>=0 and r<n_rows and c>=0 and c<n_cols and visited[r][c]!=1 and board[r][c]=='O':
                
                self.dfs(r,c,visited,n_rows,n_cols,board,possible_dir)
        
        
        
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        n_rows = len(board)
        n_cols = len(board[0])
        visited = [[0 for i in range(n_cols)] for j in range(n_rows)]
        possible_dir = [[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(n_cols):
            if board[0][i] == 'O' and visited[0][i]!=1:
                self.dfs(0,i,visited,n_rows,n_cols,board,possible_dir)
            if board[n_rows-1][i] == 'O' and visited[n_rows-1][i]!=1:
                self.dfs(n_rows-1,i,visited,n_rows,n_cols,board,possible_dir)
        for i in range(n_rows):
            if board[i][0] == 'O' and visited[i][0]!=1:
                self.dfs(i,0,visited,n_rows,n_cols,board,possible_dir)
            if board[i][n_cols-1] == 'O' and visited[i][n_cols-1]!=1:
                self.dfs(i,n_cols-1,visited,n_rows,n_cols,board,possible_dir)
        for i in range(n_rows):
            for j in range(n_cols):
                if visited[i][j] != 1 and board[i][j] == 'O':
                    board[i][j] = 'X'