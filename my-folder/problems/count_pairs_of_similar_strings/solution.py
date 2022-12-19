class Solution:
    def similarPairs(self, words: List[str]) -> int:
        l = []
        for w in words:
            l.append(set(w))
        # print(l)
        c=0
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                # print(i,j)
                if l[i]==l[j]:
                    # print(l[i],l[j])
                    c+=1
        return c
        