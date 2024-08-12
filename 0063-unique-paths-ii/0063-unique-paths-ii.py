class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1] == 1:
            return 0
        
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        memo = {}

        def dp(r, c):
            if r == 0 and c == 0:
                memo[(r, c)] = 1
                return memo[(r, c)]

            if (r, c) not in memo:
                paths = 0
                if r > 0 and obstacleGrid[r-1][c] != 1:
                    paths += dp(r-1, c)

                if c > 0 and obstacleGrid[r][c-1] != 1:
                    paths += dp(r, c-1)

                memo[(r, c)] = paths

            return memo[(r, c)]

        return dp(r-1, c-1)