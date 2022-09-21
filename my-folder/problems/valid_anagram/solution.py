class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashm = {}
        for c in s:
            if c in hashm:
                hashm[c] += 1
            else:
                hashm[c] = 1
        for c in t:
            if c in hashm:
                hashm[c] -= 1
            else:
                return False
        for i in hashm.values():
            if i != 0:
                return False
        return True
                
                
            
            
        
        