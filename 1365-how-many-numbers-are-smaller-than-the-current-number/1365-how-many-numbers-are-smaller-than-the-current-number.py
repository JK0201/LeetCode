class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        dict = {}

        for i, n in enumerate(sorted_num):
            if n not in dict:
                dict[n] = i

        return [dict[n] for n in nums]