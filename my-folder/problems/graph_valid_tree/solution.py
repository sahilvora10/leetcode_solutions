class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        # print(adj)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        # print(adj)
        queue = deque()
        queue.append((0,-1))
        visited = [-1]*n
        visited[0] = 1
        while queue:
            n,parent = queue.popleft()
            for i in adj[n]:
                if visited[i]==-1:
                    queue.append((i,n))
                    visited[i]=1
                elif visited[i]==1 and i!=parent:
                    return False
        print(visited)
        for i in visited:
            if i==-1:
                return False
        return True
                
        
        