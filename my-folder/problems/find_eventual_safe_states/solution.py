class Solution:
    def dfs_cycle_check(self,node,visited,pathvisited,graph,check):
        visited[node] = 1
        pathvisited[node] = 1
        for j in graph[node]:
            if visited[j]!= 1:
                if self.dfs_cycle_check(j,visited,pathvisited,graph,check):
                    return True
            elif visited[j] == 1 and pathvisited[j] == 1:
                return True
        check[node] = 1
        pathvisited[node] = 0
        return False
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0]*n
        pathvisited = [0]*n
        check = [0]*n
        res = []
        for i in range(n):
            if visited[i]!=1:
                self.dfs_cycle_check(i,visited,pathvisited,graph,check)
        for i in range(n):
            if check[i] == 1:
                res.append(i)
        return res
                
        