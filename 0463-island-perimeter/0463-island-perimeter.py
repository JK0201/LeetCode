from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            nonlocal cnt
            visited[r][c] = True
            q = deque()
            q.append((r, c))

            while q:
                cur_r, cur_c = q.popleft()
                
                for dr, dc in directions:
                    next_r = cur_r + dr
                    next_c = cur_c + dc

                    if 0 <= next_r < row and 0 <= next_c < col:
                        if grid[next_r][next_c] == 0:
                            cnt += 1

                        elif grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            q.append((next_r, next_c))

                    else:
                        cnt += 1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and not visited[r][c]:
                    bfs(r, c)

        return cnt