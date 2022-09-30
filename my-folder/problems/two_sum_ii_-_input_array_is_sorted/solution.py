class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = {}
        # for i,value in enumerate(numbers):
        #     rem = target - value
        #     if rem in seen:
        #         return [seen[rem],i+1]
        #     else:
        #         seen[value]=i+1
        i = 0
        j = len(numbers)-1
        while i<j:
            s = numbers[i]+numbers[j]
            if  s == target:
                return [i+1,j+1]
            elif s>target:
                j = j-1
            else:
                i = i+1