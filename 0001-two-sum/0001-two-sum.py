class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = sorted(nums)
        left = 0
        right = len(list) - 1
        result = []

        while left < right:
            calc = list[left] + list[right]

            if calc > target:
                right -= 1
            
            elif calc < target:
                left += 1
            
            else:
                break

        for idx, num in enumerate(nums):
            if num == list[left] or num == list[right]:
                result.append(idx)

        result.sort()
        return result