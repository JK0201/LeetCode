from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def bfs(r, c):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            visited[r][c] = True
            q = deque()
            q.append((r, c, 1))

            while q:
                cur_r, cur_c, dist = q.popleft()
                
                if cur_r == row -1 and cur_c == col -1:
                    return dist
                
                for dr, dc in directions:
                    next_r = cur_r + dr
                    next_c = cur_c + dc

                    if 0 <= next_r < row and 0 <= next_c < col:
                        if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            q.append((next_r, next_c, dist + 1))
            return -1
            
        return bfs(0, 0) 