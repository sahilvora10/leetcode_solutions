class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [-1]*n
        queue = deque()
        queue.append(0)
        while queue:
            x = queue.popleft()
            # print(x,rooms[x])
            visited[x] = 1
            for j in rooms[x]:
                if visited[j]==-1:
                    queue.append(j)
        # print(visited)
        for i in visited:
            if i==-1:
                return False
        return True
        