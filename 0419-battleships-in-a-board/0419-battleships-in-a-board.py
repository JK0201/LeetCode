class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        row, col = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * col for _ in range(row)]

        def dfs(cur_r, cur_c):
            visited[cur_r][cur_c] = True

            for dr, dc in directions:
                next_r = dr + cur_r
                next_c = dc + cur_c

                if 0 <= next_r < row and 0 <= next_c < col:
                    if board[next_r][next_c] == 'X' and not visited[next_r][next_c]:
                        dfs(next_r, next_c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'X' and not visited[r][c]:
                    dfs(r, c)
                    cnt += 1

        return cnt