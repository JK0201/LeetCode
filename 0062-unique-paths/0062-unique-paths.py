class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 if c == 0 or r == 0 else -1 for c in range(n)] for r in range(m)]
        
        def dp(r, c):
            if r == 0 and c == 0:
                return 1

            if memo[r][c] == -1:
                memo[r][c] = dp(r-1, c) + dp(r, c-1)

            return memo[r][c]

        return dp(m-1, n-1)