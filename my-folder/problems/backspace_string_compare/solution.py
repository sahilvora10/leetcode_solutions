class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_st = []
        for c in s:
            if s_st and c == '#':
                s_st.pop()
            elif len(s_st)==0 and c == '#':
                continue
            else:
                s_st.append(c)
        s_st = ''.join(s_st)
        t_st = []
        for c in t:
            if t_st and c == '#':
                t_st.pop()
            elif len(t_st)==0 and c == '#':
                continue
            else:
                t_st.append(c)
        t_st = ''.join(t_st)
        return s_st == t_st
                
                
                
        