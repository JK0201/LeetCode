class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def dp(n):
            if n == 0:
                return nums[n]

            if n not in memo:
                memo[n] = max(nums[n], nums[n] + dp(n-1))

            return memo[n]

        return max(dp(n) for n in range(len(nums)))