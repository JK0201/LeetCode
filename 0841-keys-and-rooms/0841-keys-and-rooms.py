class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def dfs(cur_v):
            visited[cur_v] = True
            for v in rooms[cur_v]:
                if not visited[v]:
                    dfs(v)
                    
        dfs(0)
        return False if False in visited else True