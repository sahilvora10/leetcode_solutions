class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''.join(c for c in s.lower() if c.isalnum())
        print(k)
        i = 0
        j = len(k)-1
        while(i<j):
            if k[i] == k[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        