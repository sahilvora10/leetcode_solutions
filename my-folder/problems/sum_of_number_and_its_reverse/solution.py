class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num,num//2-1,-1):
            # print(i)
            if i+int(str(i)[::-1])==num:
                # print(i)
                return True
        return False
        