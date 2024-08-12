class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1] == 1:
            return 0
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        memo = [[0] * col for _ in range(row)]

        for r in range(row):
            if obstacleGrid[r][0] == 1:
                break
            memo[r][0] = 1

        for c in range(col):
            if obstacleGrid[0][c] == 1:
                break
            memo[0][c] = 1

        for r in range(1, row):
            for c in range(1, col):
                if obstacleGrid[r][c] != 1:
                    memo[r][c] = memo[r-1][c] + memo[r][c-1]

                else: 
                    obstacleGrid[r][c] = 0

        return memo[row-1][col-1]