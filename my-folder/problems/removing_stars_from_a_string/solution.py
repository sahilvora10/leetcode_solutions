class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if st and s[i]=='*':
                st.pop()
            else:
                st.append(s[i])
        return ''.join(st)