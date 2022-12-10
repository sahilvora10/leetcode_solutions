class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxres = -1
        for s in strs:
            if s.isnumeric():
                # print(s)
                # print(int(s))
                maxres = max(maxres,int(s))
            else:
                maxres = max(maxres,len(s))
        return maxres
        