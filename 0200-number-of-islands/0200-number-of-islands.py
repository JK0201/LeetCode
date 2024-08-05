class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def dfs(cur_r, cur_c):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited[cur_r][cur_c] = True

            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc

                if 0 <= next_r < row and 0 <= next_c < col:
                    if grid[next_r][next_c] == '1' and not visited[next_r][next_c]:
                        dfs(next_r, next_c)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    cnt += 1

        return cnt