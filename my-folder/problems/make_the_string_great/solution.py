class Solution:
    def makeGood(self, s: str) -> str:
        print(s)
        s = list(s)
        # print(abs(ord('B')-ord('b')))
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if len(stack)>0:
                top = stack[-1]
                if abs(ord(s[i])-ord(top)) == 32:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return ''.join(stack)
                
            
            
         
        