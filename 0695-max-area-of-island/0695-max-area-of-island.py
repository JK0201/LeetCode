class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(cur_r, cur_c):
            nonlocal cur_area
            visited[cur_r][cur_c] = True

            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc

                if 0 <= next_r < row and 0 <= next_c < col:
                    if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                        cur_area += 1
                        dfs(next_r, next_c)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and not visited[r][c]:
                    cur_area = 1
                    dfs(r, c)
                    max_area = max(max_area, cur_area)

        return max_area