class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        sol = []
        for qu in queries:
            p,q = qu
            # print(p,q)
            cc = 0
            while p!=q:
                if p>q and p!=1:
                    p = p//2
                    cc+=1
                elif q>p and q!=1:
                    q=q//2
                    cc+=1
            sol.append(cc+1)
        return sol
            
            
        