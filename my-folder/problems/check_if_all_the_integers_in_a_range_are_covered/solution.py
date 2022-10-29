class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        x = [i for i in range(left,right+1)]
        print(x)
        for i in x:
            flag = False
            for r in ranges:
                if i>=r[0] and i<=r[1]:
                    flag = True
            if not flag:
                return False
        return True
        