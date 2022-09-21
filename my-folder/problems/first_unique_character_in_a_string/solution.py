class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashm = {}
        for c in s:
            if c in hashm:
                hashm[c] += 1
            else:
                hashm[c] = 1
        # print(hashm)
        for k,v in hashm.items():
            if v == 1:
                return s.index(k)
        return -1
        