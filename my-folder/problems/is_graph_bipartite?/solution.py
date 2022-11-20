class Solution:
    
    def bfs(self,node,graph,visited):
        queue = []
        queue.append(node)
        while len(queue)>0:
            n = queue.pop()
            for j in graph[n]:
                # print(visited)
                if visited[j] == -1:
                    queue.append(j)
                    visited[j] = 1 if visited[n] == 2 else 2
                elif visited[j]==visited[n]:
                    return False
        return True
    
    def dfs(self,node,graph,visited,color):
        visited[node] = color
        for j in graph[node]:
            if visited[j] == -1:
                c = 1 if color == 2 else 2
                if not self.dfs(j,graph,visited,c):
                    return False
            elif visited[j] == visited[node]:
                return False
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        visited = [-1]*n
        for i in range(n):
            if visited[i]==-1:
                 if not self.dfs(i,graph,visited,1):
                        return False
        return True
        