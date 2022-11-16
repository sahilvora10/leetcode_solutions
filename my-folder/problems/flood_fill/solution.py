class Solution:
    def dfs(self,i,j,image,n_rows,n_cols,possible_dir,target_color,init_color):
        image[i][j] = target_color
        for p in possible_dir:
            r,c = i+p[0],j+p[1]
            if r>=0 and r<n_rows and c>=0 and c<n_cols and image[r][c]==init_color and image[r][c]!=target_color:
                self.dfs(r,c,image,n_rows,n_cols,possible_dir,target_color,init_color)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n_rows = len(image)
        n_cols = len(image[0])
        init_color = image[sr][sc]
        possible_dir = [[-1,0],[1,0],[0,-1],[0,1]]
        self.dfs(sr,sc,image,n_rows,n_cols,possible_dir,color,init_color)
        return image
        
        