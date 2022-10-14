class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = [False]*len(candies)
        maxc = max(candies)
        for i in range(len(candies)):
            ans[i] = candies[i]+extraCandies >= maxc
        return ans
        