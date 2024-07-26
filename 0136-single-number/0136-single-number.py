class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}

        for n in nums:
            if n not in dict:
                dict[n] = 1

            else:
                dict[n] += 1

        for k, v in dict.items():
            if v == 1:
                return k