class Solution:
    def dfs(self,node,parent,visited,adj,seats):
        
        visited[node] = 1
        # print(node,parent,visited)
        cnt = 1
        for j in adj[node]:
            if visited[j]!=1:
                cnt += self.dfs(j,node,visited,adj,seats)
        if node!=0:
            self.fuel += math.ceil(cnt/seats)
            # print(self.fuel)
        return cnt
        
        
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads)
        adj = [[] for i in range(n+1)]
        for r in roads:
            adj[r[1]].append(r[0])
            adj[r[0]].append(r[1])
            
        # print(adj)
        visited = [-1]*(n+1)
        self.fuel = 0
        self.dfs(0,-1,visited,adj,seats)
        return self.fuel
        
    
        