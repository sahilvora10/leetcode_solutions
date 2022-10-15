import math
class Solution:
    def getpowerarray(self,n):
        binary = bin(n).replace("0b","")[::-1]
        arr = []
        for i in range(len(binary)):
            if binary[i]=='1':
                arr.append(2**i)
        return arr
            
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        pa= self.getpowerarray(n)
        # print(pa)
        res = []
        for q in queries:
            res.append((math.prod(pa[q[0]:q[1]+1])%(10**9 + 7)))
        return res