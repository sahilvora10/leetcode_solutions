class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hp = defaultdict(int)
        for a in arr:
            hp[a]+=1
        if len(set(hp.values()))!=len(set(arr)):
            return False
        return True
        
        