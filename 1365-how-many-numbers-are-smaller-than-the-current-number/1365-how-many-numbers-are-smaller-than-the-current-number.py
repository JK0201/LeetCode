class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and nums[i] > nums[j]:
                    cnt += 1

            res.append(cnt)

        return res