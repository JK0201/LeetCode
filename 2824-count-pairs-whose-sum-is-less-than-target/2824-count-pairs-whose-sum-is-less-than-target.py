class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    cnt += 1

        return cnt