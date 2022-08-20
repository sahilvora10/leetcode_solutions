class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # maxAns = 0
        # for a in accounts:
        #     maxAns = max(maxAns,sum(a))
        return max(map(sum,accounts))
    
        