class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x >= 0 and str(x) == str(x)[::-1]:
        #     return True
        # return False
        if x < 0 or (x>0 and x%10 == 0):
            return False
        revx = 0
        while (x > revx):
            revx = revx*10 + x%10
            x = x//10
        
        return True if x == revx or x == revx//10 else False
        