class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        # ss = 0
        # for i in range(len(t)):
        #     if ss < len(s):
        #         print(s[ss])
        #         if s[ss] == t[i]:
        #             ss+=1
        # return True if ss==len(s) else False
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        print(i,j)
        if i==len(s):
            return True
        else:
            return False
