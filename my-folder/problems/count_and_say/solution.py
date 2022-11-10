class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        s = "11"
        for j in range(3,n+1):
            count = 1
            tmp = ""
            s += "$"
            l = len(s)
            for i in range(1,l):
                if s[i] == s[i-1]:
                    count +=1
                else:
                    tmp += str(count)
                    tmp += s[i-1]
                    #print(tmp)
                    count = 1
            s = tmp
        return s
            
        