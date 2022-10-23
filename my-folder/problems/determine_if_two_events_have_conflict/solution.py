class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1 = event1[0]
        e1 = event1[1]
        s2 = event2[0]
        e2 = event2[1]
        s1 = (int(s1[0:2])+(0.01*int(s1[3:5])))
        e1 = (int(e1[0:2])+(0.01*int(e1[3:5])))
        s2 = (int(s2[0:2])+(0.01*int(s2[3:5])))
        e2 = (int(e2[0:2])+(0.01*int(e2[3:5])))
        print(s1,e1,s2,e2)
        if s1>=s2 and s1<=e2:
            return True
        if e1>=s2 and e1<=e2:
            return True
        if s2>=s1 and  s2<=e1:
            return True
        if e2>=s1 and e2<=e1:
            return True