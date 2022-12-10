class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(vals[e[1]])
            adj[e[1]].append(vals[e[0]])
        # print(adj)
        maxres = -10000000000000004
        for i in range(n):
            s = vals[i]
            maxk = sorted(adj[i],reverse=True)[:k]
            maxkk = [x for x in maxk if x>=0]
            sadj = sum(maxkk)
            # print(i,s,sadj)
            if s+sadj>=s:
                s+=sadj
            # print(i,s)
            maxres = max(maxres,s)
        return maxres
        