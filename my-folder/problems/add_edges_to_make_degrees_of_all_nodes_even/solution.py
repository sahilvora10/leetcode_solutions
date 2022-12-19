class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n+1)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        # print(adj)
        odd = [i for i in range(1,len(adj)) if len(adj[i])%2!=0]
        # print(odd)
        
        #if number of odd nodes is odd then not possible
        if len(odd)%2!=0:
            return False
        
        #if number of odd nodes ==0 :true
        if len(odd)==0:
            return True
        
        #if number of odd nodes>4 : false as max 2 edges allowed
        if len(odd)>4:
            return False
        
        #if number of odd nodes==4, can only connect between themself as if connect to some other node, would need more than 2 edges
        if len(odd)==4:
            if (odd[1] not in adj[odd[0]] and odd[3] not in adj[odd[2]]) or (odd[2] not in adj[odd[0]] and odd[3] not in adj[odd[1]]) or (odd[3] not in adj[odd[0]] and odd[1] not in adj[odd[2]]):
                return True
            
        #if number of odd nodes ==2, try to connect with any other node
        if len(odd)==2:
            # print('here')
            for i in range(1,n+1):
                if odd[0] not in adj[i] and odd[1] not in adj[i]:
                    return True
        
        return False
        
        