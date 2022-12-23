class Solution:
    def intToRoman(self, num: int) -> str:
        hp = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'   
        }
        ans = ""
        p = 3
        while p>=0:
            th = num//(10**p)
            r = num%(10**p)
            if th-5<=0 or th==9:
                if th*(10**p) in hp:
                    ans+=hp[th*(10**p)]
                else:
                    ans+=hp[10**p]*th
            else:
                ans+=hp[5*(10**p)]
                ans+=hp[(10**p)]*(th-5)
            num = r
            p-=1
        return ans
    
        