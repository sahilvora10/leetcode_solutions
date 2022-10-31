class Solution:
    def oddString(self, words: List[str]) -> str:
        hashmap = defaultdict(list)
        for w in words:
            diff = []
            for i in range(1,len(w)):
                diff.append(ord(w[i])-ord(w[i-1]))
            hashmap[tuple(diff)].append(w)
        for s in hashmap:
            if len(hashmap[s]) == 1:
                return hashmap[s][0]
        