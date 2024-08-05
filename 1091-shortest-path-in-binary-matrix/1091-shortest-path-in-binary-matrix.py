from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        shortest_path = -1
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        q = deque()
        q.append((0, 0, 1))
        visited[0][0] = True

        while q:
            cur_r, cur_c, dist = q.popleft()

            if cur_r == row - 1 and cur_c == col - 1:
                shortest_path = dist
                break

            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc

                if 0 <= next_r < row and 0 <= next_c < col:
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        q.append((next_r, next_c, dist + 1))

        return shortest_path