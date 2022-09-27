class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        # print(s)
        r = ""
        positive = True
        if s == "":
            return 0
        if s[0]=="-":
            positive = False
            s = s[1:]
        elif s[0] == '+':
            s= s[1:]
        else:
            s = s
        for c in s:
            if c.isnumeric():
                r += c
            else:
                break
        print(r)
        if r=="":
            return 0
        else:
            if positive:
                a = int(r)
                if a>(2**31 - 1):
                    return 2**31 -1
                else:
                    return a
            else:
                a = -1*int(r)
                if a<-2**31:
                    return -2**31
                else:
                    return a
            
            
        