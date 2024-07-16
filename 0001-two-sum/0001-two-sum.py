class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for idx, key in enumerate(nums):
            req = target - key

            if req in dict.keys():
                return [dict[req], idx]

            dict[key] = idx