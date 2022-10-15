class Solution:
    def countTime(self, time: str) -> int:
        ans = 1
        if time[3]=='?': ans*=6
        if time[4]=='?': ans*=10
        if time[0]=='?':
            if time[1]=='?': ans*=24
            elif int(time[1]) >=0 and int(time[1])<=3:
                ans*=3
            else:
                ans*=2
        elif time[1]=='?':
            if int(time[0]) ==0 or int(time[0])==1:
                ans*=10
            else:
                ans*=4
        return ans
        
        