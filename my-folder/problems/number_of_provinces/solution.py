class Solution:
    
    def dfs(self,node,isConnected,visited):
        visited[node] = 1
        # dfs_res.append(node+1)
        for r in range(len(isConnected)):
            if node != r and isConnected[node][r] == 1 and visited[r]!=1:
                self.dfs(r,isConnected,visited)
    
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n
        count = 0
        for i in range(n):
            # dfs_res = []
            if visited[i] == 0:
                count+=1
                self.dfs(i,isConnected,visited)
                # print(dfs_res)
        return count