from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        res = False
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = [False] * len(graph)

        q = deque()
        q.append(source)
        visited[source] = True

        while q:
            cur_v = q.popleft()

            if cur_v == destination:
                res = True
                break

            for v in graph[cur_v]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        return res