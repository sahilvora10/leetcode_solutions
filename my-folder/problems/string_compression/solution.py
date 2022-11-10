class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        chars.append('0')
        i = 0
        j = 0
        write = 0
        count =0
        le = len(chars)
        while j<len(chars):
            if j ==le or chars[j] != chars[i]:
                chars[write] = chars[i]
                write += 1
                
                if count > 1:
                    for cntc in str(count):
                        chars[write] = cntc
                        write += 1
                    
                count = 0
                i = j
            else:
                count += 1
                j += 1
        return write
        
        
        
        