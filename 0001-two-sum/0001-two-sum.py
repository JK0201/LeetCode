class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}

        for idx, key in enumerate(nums):
            req = target - key

            if req in list.keys():
                return [list[req], idx]

            list[key] = idx