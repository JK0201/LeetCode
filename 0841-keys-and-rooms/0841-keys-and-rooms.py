from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited =  [False] * len(rooms)

        q = deque()
        q.append(0)
        visited[0] = True

        while q:
            cur_v = q.popleft()

            for v in rooms[cur_v]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        return False if False in visited else True