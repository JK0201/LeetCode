from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        colored = [[image[r][c] for c in range(col)] for r in range(row)]
        visited = [[False] * col for _ in range(row)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            visited[r][c] == True
            q = deque()
            q.append((r, c))

            while q:
                cur_r, cur_c = q.popleft()
                colored[cur_r][cur_c] = color

                for dr, dc in directions:
                    next_r = cur_r + dr
                    next_c = cur_c + dc

                    if 0 <= next_r < row and 0 <= next_c < col:
                        if image[next_r][next_c] == image[cur_r][cur_c] and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            q.append((next_r, next_c))

        bfs(sr, sc)
        return colored
