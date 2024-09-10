import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        visited = {}

        for i, t in enumerate(times):
            if t[0] not in graph:
                graph[t[0]] = [(t[2], t[1])]

            else:
                graph[t[0]].append((t[2], t[1]))

            visited[t[0]] = visited[t[1]] = False
        
        def solution(graph, start, final):
            costs = {}
            pq = []
            visited[start] = True
            heapq.heappush(pq, (0, start))
            
            while pq:
                cur_cost, cur_v = heapq.heappop(pq)
                if cur_v not in costs:
                    costs[cur_v] = cur_cost
                    
                    if cur_v in graph:
                        for cost, next_v in graph[cur_v]:
                            next_cost = cur_cost + cost
                            visited[next_v] = True
                            heapq.heappush(pq, (next_cost, next_v))
                        
            return costs

        minCostDict = solution(graph, k, n)

        for v in visited.values():
            if v == False:
                print(v)
                return -1

        return minCostDict[n]