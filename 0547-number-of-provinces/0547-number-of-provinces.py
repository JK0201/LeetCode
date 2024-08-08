class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        visited = [False] * len(isConnected)

        def dfs(cur_c):
            visited[cur_c] = True
            city = isConnected[cur_c]
            
            for i in range(len(city)):
                if city[i] == 1 and not visited[i]:
                    dfs(i)

        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                cnt += 1

        return cnt