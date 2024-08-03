class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            right -= nums[i]
            res[i] = abs(left - right)
            left += nums[i]

        return res