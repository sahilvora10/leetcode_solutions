class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        temperatures = temperatures[::-1]
        # print(temperatures)
        for i,curr in enumerate(temperatures):
            res = 0
            while stack and stack[-1][0]<=curr:
                stack.pop()
            ans[i] = i - stack[-1][1] if stack else 0
            stack.append([curr,i])
            # print(stack)
        return ans[::-1]
        