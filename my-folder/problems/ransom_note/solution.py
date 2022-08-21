class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # dm = {e:magazine.count(e) for e in set(magazine)}
        # dr = {e:ransomNote.count(e) for e in set(ransomNote)}
        # # print(dm,dr)
        # f = True
        # for i in dr:
        #     if i not in dm or dr[i] > dm[i]:
        #         f = False
        #         break
        # return f
        c = 0
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,"",1)
                c+=1
        return c == len(ransomNote)
        