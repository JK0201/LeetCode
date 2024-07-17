class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        count = 1
        max_length = 1

        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1

                else:
                    max_length = max(count, max_length)
                    count = 1

        max_length = max(count, max_length)
        return max_length