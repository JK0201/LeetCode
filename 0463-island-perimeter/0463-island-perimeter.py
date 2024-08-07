from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        row, col = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        next_r = r + dr
                        next_c = c + dc

                        if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col or grid[next_r][next_c] == 0:
                            cnt += 1
        return cnt