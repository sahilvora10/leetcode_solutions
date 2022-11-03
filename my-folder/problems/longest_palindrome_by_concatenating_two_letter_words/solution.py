class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hm = {}
        for w in words:
            if w in hm:
                hm[w] += 1
            else:
                hm[w] = 1
        print(hm)
        count = 0
        flag = False
        for w in words:
            r = w[::-1]
            if w!=r and w in hm and hm[w]>0 and r in hm and hm[r]>0:
                count+=4
                hm[w]-=1
                hm[r]-=1
            elif w==r and w in hm and hm[w]>1:
                count+=4
                hm[w]-=2
            elif w==r and not flag and w in hm and hm[w]>0:
                count+=2
                hm[w]-=1
                flag = True
        return count
        