class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0 or source == destination:
            return True
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        # print(adj)
        visited = [0]*n
        queue = deque()
        queue.append(source)
        visited[source] = 1
        while len(queue)>0:
            node = queue.popleft()
            # print(node)
            for j in adj[node]:
                if visited[j]!=1:
                    if j == destination:
                        # print(j)
                        return True
                    visited[j] = 1
                    queue.append(j)
        return False
        