from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        row, col = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            image[r][c] = color

            while q:
                cur_r, cur_c = q.popleft()

                for dr, dc in directions:
                    next_r = cur_r + dr
                    next_c = cur_c + dc

                    if 0 <= next_r < row and 0 <= next_c < col:
                        if image[next_r][next_c] == originalColor:
                            image[next_r][next_c] = color
                            q.append((next_r, next_c))

        bfs(sr, sc)
        return image
