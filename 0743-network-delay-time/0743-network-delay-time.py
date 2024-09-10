class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False] * n
        graph = {k + 1 : [] for k in range(n)}
        
        for t in times:
            graph[t[0]].append((t[2], t[1]))

        def dijkstra(graph, start):
            costs = {}
            pq = []
            visited[start-1] = True
            heapq.heappush(pq, (0, start))

            while pq:
                cur_cost, cur_v = heapq.heappop(pq)
                if cur_v not in costs:
                    costs[cur_v] = cur_cost

                    for cost, next_v in graph[cur_v]:
                        if not visited[next_v-1]:
                            next_cost = cur_cost + cost
                            visited[next_v-1] = True
                            heapq.heappush(pq, (next_cost, next_v))

            return costs

        costs = dijkstra(graph, k)        
        
        falseCnt = visited.count(False)
        if falseCnt > 0:
            return -1

        else:
            return max(costs.values())