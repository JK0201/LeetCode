class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {k + 1 : [] for k in range(len(edges) + 1)}

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        for k, v in graph.items():
            if len(v) > 1:
                return k