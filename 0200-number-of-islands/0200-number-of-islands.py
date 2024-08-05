class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def dfs(r, c):
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            visited[r][c] = True

            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]

                if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                    if grid[next_r][next_c] == '1' and not visited[next_r][next_c]:
                        dfs(next_r, next_c)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    cnt += 1

        return cnt