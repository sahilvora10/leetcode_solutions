class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # r = []
        # c = 1
        # for n in digits[::-1]:
        #     c += n
        #     if c >=10 :
        #         r.insert(0,c%10)
        #         c = c//10
        #     else:
        #         r.insert(0,c)
        #         c = 0
        #     print(r)
        # if c>=1:
        #     r.insert(0,c)
        # return r
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits
            
        
        # n = len(digits)
        # s = 0
        # #123
        # for l in digits:
        #     s += l*(10**(n-1))
        #     print(s)
        #     n -= 1
        # return [*str(s+1)]
        
        