class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([(len(str(i))+1)%2 for i in nums])
        