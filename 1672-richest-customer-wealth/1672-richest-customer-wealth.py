class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0

        for a in accounts:
            wealth = max(sum(a), wealth)

        return wealth