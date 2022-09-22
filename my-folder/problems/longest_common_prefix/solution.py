class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        #min len
        minl = len(strs[0])
        for s in strs:
            minl = min(minl,len(s))

        res = ""
        for i in range(minl):
            current_char = strs[0][i]
            for j in strs:
                if j[i] != current_char:
                    return res
            res = res + current_char
        return res
            
            
        
    