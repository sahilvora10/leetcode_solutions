class Solution:
    def pathSum(self, nums: List[int]) -> int:
        graph = defaultdict(int)
        for num in nums:
            depth, pos, val = num//100-1, (num//10)%10-1, num%10
            graph[depth, pos] = val
        # print(graph)
        ts = 0
        stack = deque()
        stack.append((graph[0,0],0,0))
        # print(stack)
        while stack:
            currsum,l,i = stack.pop()
            if (l+1,2*i) not in graph and (l+1,2*i+1) not in graph:
                ts+=currsum
            if (l+1,2*i) in graph:
                stack.append((currsum+graph[(l+1,2*i)],l+1,2*i))
            if (l+1,2*i+1) in graph:
                stack.append((currsum++graph[(l+1,2*i+1)],l+1,2*i+1))
            # print(stack)
        return ts
        