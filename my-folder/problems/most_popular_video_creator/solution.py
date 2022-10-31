class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        hashmap = {}
        maxc = 0
        res = []
        for i in range(len(creators)):
            if creators[i] in hashmap:
                hashmap[creators[i]][0] += views[i]
                if hashmap[creators[i]][2] < views[i]:
                    hashmap[creators[i]][1] = ids[i]
                    hashmap[creators[i]][2] = views[i]
                if hashmap[creators[i]][2] == views[i]:
                    hashmap[creators[i]][1] = min(hashmap[creators[i]][1],ids[i])
            else:
                hashmap[creators[i]] = [views[i],ids[i],views[i]]
            maxc = max(hashmap[creators[i]][0],maxc)
        for i in hashmap:
            if hashmap[i][0] == maxc:
                res.append([i,hashmap[i][1]])
        return res
        
        