class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dfs(n):
            if n == 0 or n == 1:
                return 0

            if n not in memo:
                memo[n] = min(dfs(n-1) + cost[n-1],dfs(n-2) + cost[n-2] )

            return memo[n]
            
        return dfs(n)