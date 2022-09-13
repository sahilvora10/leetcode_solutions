class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s,t):
            map_s = {}
            map_t = {}
            for i in range(len(s)):
                if (s[i] in map_s.keys() and map_s[s[i]] != t[i]) or (t[i] in map_t.keys() and map_t[t[i]]!=s[i]) :
                    return False
                map_s[s[i]] = t[i]
                map_t[t[i]] = s[i]
            return True
        
        return check(s,t)
        