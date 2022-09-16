class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        i = 0
        for j in range(1,len(prices)):
            if prices[j]>prices[i]:
                maxprofit= max(maxprofit,prices[j]-prices[i])
            else:
                i=j
        return maxprofit
        